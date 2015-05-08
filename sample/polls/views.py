from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Question
def index(request):
	latest_question_list = Question.objects.order_by('-pdate')[:3]
    	output = {'latest_question_list':latest_question_list}
    	return render(request, 'polls/index.html', output)
def detail(request, question_id):
	try:
		q = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404("Question doesn't exist")
	return render(request, 'polls/detail.html', {'question':q})
def results(request, question_id):
	return ("Currently at results of Question %s." %question_id)
def vote(request, question_id):
	return HttpResponse("Voting for Question %s."%question_id)
