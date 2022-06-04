from django.db import models

# Create your models here.
from account.models import Student
from course.models import Lesson


class Evaluation(models.Model):
    instructions = models.TextField(blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    revise = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.instructions},{self.lesson},{self.student},{self.is_available}'


class EvaluationQuestion(models.Model):
    question = models.CharField(max_length=200)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.question},{self.evaluation}'


class EvaluationAnswer(models.Model):
    answer = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    evaluation_question = models.ForeignKey(EvaluationQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.answer},{self.is_correct},{self.evaluation_question}'
