#from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import get_object_or_404, get_list_or_404,render, redirect
from django.http import Http404
# from .models import Question, Choice

from django.views import generic
from django.urls import reverse

# from .forms import QuestionForm
from django.utils import timezone

# MongoDB
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Post
import datetime

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
# # Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
#     context = {
#         'latest_question_list' : latest_question_list,
#     }
#     # template = loader.get_template('polls/index.html')
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)
    
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404('Question does not exist')
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html',{
#             'question': question,
#             'error_message': "you didn't select a choice"
#         })
#     else:
#         selected_choice.votes +=1
#         selected_choice.save()

#         return HttpResponseRedirect(reverse('polls:results',args=(question.id,)) )

# def ques_new(request):
#     if request.method == "POST":
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.question_text = request.question_text
#             post.pub_date = timezone.now()
#             post.save()
#             return redirect('detail', pk=post.pk)
#     else:
#         form = QuestionForm()
#     return render(request, 'polls/ques_edit.html',{'form': form} )
    
def mongo(request):
   if request.method == 'POST':
      #save new post
      title = request.POST['title']       
      content = request.POST['content']
      post = Post(title=title)
      post.last_update = datetime.datetime.now() 
      post.content = content
      post.save()

   #Get all posts from DB
   posts = Post.objects 
   return render(request, 'polls/indexMongo.html', {'Posts': posts} )
   #  return render_to_response('polls/indexMongo.html', {'Posts': posts},
   #                            context_instance=RequestContext(request))