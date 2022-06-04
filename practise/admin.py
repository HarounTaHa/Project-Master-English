from django.contrib import admin
from .models import Practise, PractiseQuestionOne, AnswerQuestionOne, PractiseQuestionTwo, AnswerQuestionTwo
# Register your models here.
admin.site.register(
    [Practise, PractiseQuestionOne, AnswerQuestionOne, PractiseQuestionTwo, AnswerQuestionTwo])
