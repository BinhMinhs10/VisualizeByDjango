# To create a URLconf
from django.urls import path
from . import views

app_name = 'hotels'
urlpatterns = [
    # ex: /polls
    path('', views.index, name='index'),
    # ex: /polls/5
    # the 'name' value as called by the {% url %} template tag
    # path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results
    #path('<int:question_id>/results/', views.result, name='results'),
    # ex: /polls/5/vote
    #path('<int:question_id>/vote/', views.vote, name='vote')
]