from django.db import models
from .user import User
from .question import Question

class BadQuestionReport(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    userDescription = models.CharField(max_length=1000)
    problemCategory = models.CharField(max_length=1000)
    date = models.DateField(auto_now=True)
