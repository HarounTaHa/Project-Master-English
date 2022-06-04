from django.db import models

# Create your models here.
from account.models import Student
from department.models import Department


class Course(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True, through='StudentProgressInCourse')
    course_name = models.CharField(max_length=100)
    number_of_lessons = models.IntegerField(default=0)

    def __str__(self):
        return self.course_name


class StudentProgressInCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'course: {self.course.course_name} , Name: {self.student}'


class Lesson(models.Model):
    objective = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, blank=True, through='StudentProgressInLesson')
    content = models.FileField(upload_to='lessons/', blank=True)

    #
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.course.number_of_lessons += 1
            self.course.save()
            return super().save(*args, **kwargs)
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.course:
            self.course.number_of_lessons -= 1
            self.course.save()
            return super().delete(*args, **kwargs)
        return super().delete(*args, **kwargs)

    def __str__(self):
        return f'Objective : {self.objective[:50]}, Name:{self.course.course_name}'


class StudentProgressInLesson(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return f'Name: {self.student},  {self.lesson}'


class WarmUp(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='warmUp_lesson')
    warm_up = models.FileField(upload_to='lessons/', blank=True)

    def __str__(self):
        return f'{self.lesson},{self.warm_up}'

class WarmUpQuestion(models.Model):
    question = models.CharField(max_length=200)
    warm_up = models.ForeignKey(WarmUp, on_delete=models.CASCADE)

    def __str__(self):
        return self.question


class WarmUpAnswer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(WarmUpQuestion, on_delete=models.CASCADE)

    def __str__(self):
        return f"question:{self.question}, answer: {self.text}, correct : {self.correct}"
