#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404,render
from django.http import Http404
# from .models import Question, Choice

from django.views import generic
from django.urls import reverse

from elasticsearch import Elasticsearch


# Create your views here.
def index(request):
    if request.method == 'POST':
        es = Elasticsearch()
        res = es.search(index="newpapers", doc_type="post", body={"query": {"match": {"content": request.POST['textsearch'] }}})
        results=[]
        for post in res['hits']['hits']:
            result = post['_source']
            results.append(result)
        return render(request, 'elasticsearchs/index.html',{
            'time': res['took'],
            'total': res['hits']['total'],
            'results': results
        })
    return render(request, 'elasticsearchs/index.html')
