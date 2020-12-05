from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length = 200)
    question_number = models.IntegerField(default = 0)
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return "Вопрос №{}: {}".format(self.question_number, self.question_text)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    answer_text = models.CharField(max_length = 200)
    answer_number = models.IntegerField(default = 0)
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return "Ответ №{}: {}".format(self.answer_number, self.answer_text)

