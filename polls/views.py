from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Answer

# def index(request):
#     all_questions = Question.objects.filter(is_active = True)
#     return render(request, 'index.html', {'all_questions' : all_questions})

def index(request):
    all_questions = Question.objects.all()
    template = loader.get_template('index.html')
    context = {'all_questions' : all_questions}
    return HttpResponse(template.render(context, request))

def question_details(request, question_id):
    question = Question.objects.get(pk = question_id)
    return render(request, 'question_details.html', {'question' : question})

def choice_made(request):
    answer_id = request.POST.get('answer')
    answer = Answer.objects.get(pk = answer_id)
    answer.votes += 1
    answer.save()
    return render(request, 'choice_made.html')

def results(request):
    all_answers = Answer.objects.all()
    template = loader.get_template('results.html')
    context = {'all_answers' : all_answers}
    return render(context, request)