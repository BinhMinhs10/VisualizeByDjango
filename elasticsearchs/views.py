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
        
        took, total, results = fuzzy_search("description",request.POST['textsearch'])
        
        return render(request, 'elasticsearchs/index.html',{
            'time': took,
            'total': total,
            'results': results
        })
        # es = Elasticsearch()
        # text = 'ra'
        # suggest_dictionary = {
        #     "entity-suggest" : {
        #             'text' : text,
        #             "completion" : {
        #                 "field" : "suggest"
        #             }
        #         }
        #     }

        # query_dictionary = {'suggest' : suggest_dictionary}

        # res = es.search(
        #     index='newpapers',
        #     doc_type='_doc',
        #     body=query_dictionary)
        # return res

    return render(request, 'elasticsearchs/index.html')
