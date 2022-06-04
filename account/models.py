from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from base.models import Departmant, Exam, Lesson


class User(AbstractUser):
    """
    Implement user model
    """
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(blank=True, unique=True)


# generate token for every user created
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
#


class Student(models.Model):
    """
    Implement student mode
    """
    is_student = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username



# class Grade(models.Model):
#     """
#     Implement Grade model
#     """
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     departmant = models.ForeignKey(Departmant, on_delete=models.CASCADE)
#     lesson_accomplished = models.IntegerField(default=0)
#     pas_exam = models.BooleanField(default=False)
#     Exam_score = models.CharField(max_length=255, blank=True, null=True, verbose_name="Student Test Score")
