from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('question/<int:question_id>/', views.question_details, name = 'question'),
    path('choice_made/', views.choice_made, name = 'choice_made'),
    path('test/', views.test, name = 'test'),
]