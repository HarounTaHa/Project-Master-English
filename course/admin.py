from django.contrib import admin
from .models import Course, Lesson, WarmUp, WarmUpQuestion, WarmUpAnswer, StudentProgressInCourse, \
    StudentProgressInLesson

# Register your models here.
admin.site.register(
    [Course, Lesson, WarmUp, WarmUpQuestion, WarmUpAnswer, StudentProgressInCourse, StudentProgressInLesson])
