from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404,render
from django.http import Http404
# from .models import Question, Choice

from django.views import generic
from django.urls import reverse

# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image
from keras.models import model_from_json

from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):

    

    # an example image
    # import matplotlib.pyplot as plt
    # plt.imshow(image.reshape(img_x, img_y, 3))
    # plt.title(brands[Y_pred[0]])
    # plt.show()
    if request.method == 'POST' and request.FILES['imgInp']:
        if request.POST['model']=='1':
            myfile = request.FILES['imgInp']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            
            brands = ['Chery', 'Mazda', 'VW', 'Citroen', 'Lexus', 'Hyundai', 'Buick', 'Peugeot', 'Honda', 'Toyota']
            img_x = img_y = 70

            # bring images back size (20778, 50, 50,3)
            def ImageConvert(img):
                im_ex = img.reshape(img_x, img_y, 3)
                im_ex = im_ex.astype('float32') / 255
                # zero center data
                im_ex = np.subtract(im_ex, 0.5)
                # ...and to scale it to (-1, 1)
                im_ex = np.multiply(im_ex, 2.0)
                return im_ex


            # loading all images
            image = Image.open('.'+uploaded_file_url).convert('LA').convert("RGB")
            image = image.resize((img_x, img_y), Image.ANTIALIAS)
            image = np.array(image).flatten()

            img = ImageConvert(image)

            # Model reconstruction from JSON file
            with open('model_architecture.json', 'r') as f:
                model = model_from_json(f.read())

            # Load weights into the new model
            model.load_weights('model_weights.h5')

            Y_pred = model.predict_classes(np.array([img, ]) )
            return render(request, 'logos/index.html', {
                'brand': brands[Y_pred[0]],
                'imglogo': uploaded_file_url
            })
        else:
            myfile = request.FILES['imgInp']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)

            
            cars = ['Alfa Romeo', 'Audi', 'BMW', 'Chevrolet', 'Citroen', 'Dacia', 'Daewoo', 'Dodge',
                'Ferrari', 'Fiat', 'Ford', 'Honda', 'Hyundai', 'Jaguar', 'Jeep', 'Kia', 'Lada',
                'Lancia', 'Land Rover', 'Lexus', 'Maserati', 'Mazda', 'Mercedes', 'Mitsubishi',
                'Nissan', 'Opel', 'Peugeot', 'Porsche', 'Renault', 'Rover', 'Saab', 'Seat',
                'Skoda', 'Subaru', 'Suzuki', 'Tata', 'Tesla', 'Toyota', 'Volkswagen', 'Volvo']
            img_x = img_y = 50

            # bring images back size (20778, 50, 50,3)
            def ImageConvert(img):
                im_ex = img.reshape(img_x, img_y, 3)
                im_ex = im_ex.astype('float32') / 255
                # zero center data
                im_ex = np.subtract(im_ex, 0.5)
                # ...and to scale it to (-1, 1)
                im_ex = np.multiply(im_ex, 2.0)
                return im_ex


            # loading all images
            image = Image.open('.'+uploaded_file_url).convert('LA').convert("RGB")
            image = image.resize((img_x, img_y), Image.ANTIALIAS)
            image = np.array(image).flatten()

            img = ImageConvert(image)

            # Model reconstruction from JSON file
            with open('model_car_ResNet_AUGM.json', 'r') as f:
                model = model_from_json(f.read())

            # Load weights into the new model
            model.load_weights('car_ResNet_AUGM_weights.h5')

            # Returns a compiled model identical to the previous one
            #model = load_model('car_ResNet_AUGM.h5py')

            Y_pred = model.predict(np.array([img, ]) )
            Y_preds={}
            for index in Y_pred.argsort()[0][-3:]:
                Y_preds[cars[index]] = Y_pred[0][index]*100

            return render(request, 'logos/index.html', {
                'brand': Y_preds,
                'imglogo': uploaded_file_url
            })
    return render(request, 'logos/index.html')
    





