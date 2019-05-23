#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404,render
from django.http import Http404
# from .models import Question, Choice

from django.views import generic
from django.urls import reverse

from elasticsearchs.searchs import *


# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST['search_type']=='1':
            took, total, results = match_phrase_prefix("description",request.POST['textsearch'])
        elif request.POST['search_type']=='2':
            took, total, results = multi_match(["title","description"],request.POST['textsearch'])
        elif request.POST['search_type']=='3':
            took, total, results = fuzzy_search("description",request.POST['textsearch'])
        elif request.POST['search_type']=='4':
            took, total, results = boolean_search_must("description",request.POST['textsearch'])
        elif request.POST['search_type']=='5':
            took, total, results = boolean_search_should("description",request.POST['textsearch'])
        elif request.POST['search_type']=='6':
            took, total, results = match("description",request.POST['textsearch'])
        else:
            took, total, results = match_phrase_prefix("description",request.POST['textsearch'])
        
        

        return render(request, 'elasticsearchs/index.html',{
            'time': took,
            'total': total,
            'results': results
        })
        

    return render(request, 'elasticsearchs/index.html')
