from django.db import models

# Create your models here.
from account.models import Student
from course.models import Lesson


class Practise(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student},{self.lesson}'


class PractiseQuestionOne(models.Model):
    question_one = models.CharField(max_length=200)
    practise = models.ForeignKey(Practise, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'PractiseQuestionOne'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.question_one},{self.practise}'


class AnswerQuestionOne(models.Model):
    answer = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(PractiseQuestionOne, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'AnswerQuestionOne'
        verbose_name_plural = verbose_name


    def __str__(self):
        return f'{self.answer},{self.correct}'


#
class PractiseQuestionTwo(models.Model):
    question_two = models.CharField(max_length=200)
    practise = models.ForeignKey(Practise, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'PractiseQuestionTwo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.question_two},{self.practise}'


#
class AnswerQuestionTwo(models.Model):
    answer = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(PractiseQuestionTwo, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'AnswerQuestionTwo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.answer},{self.correct}'
