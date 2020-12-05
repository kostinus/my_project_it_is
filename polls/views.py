from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question, Answer

def index(request):
    all_questions = Question.objects.filter(is_active = True)
    return render(request, 'index.html', {'all_questions': all_questions})
