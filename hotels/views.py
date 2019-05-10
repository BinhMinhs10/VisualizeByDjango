#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404,render
from django.http import Http404
# from .models import Question, Choice

from django.views import generic
from django.urls import reverse

# class DetailView(generic.DetailView):
    # model = Question
    # template_name = 'hotels/detail.html'
# Create your views here.
def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))
    return render(request, 'hotels/index.html')
    