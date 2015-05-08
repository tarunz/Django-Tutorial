from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.core.urlresolvers import reverse
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
	q= get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/result.html', {'question':q})
def vote(request, question_id):
	e = get_object_or_404(Question, pk=question_id)
	try:
		sel_choice = e.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		p ={'question': e, 'error_message': "Are you sure you made a decision?"}
		return render (request, 'polls/detail.html', p)
	else:
		sel_choice.votes+=1
		sel_choice.save()

	return HttpResponseRedirect(reverse('polls:result', args=(int(e.id),)))
