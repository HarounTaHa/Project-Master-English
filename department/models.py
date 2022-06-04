from django.db import models


# Create your models here.


class Department(models.Model):
    OPTIONS = (
        ['listening', 'Listening'],
        ['speaking', 'Speaking'],
    )
    department = models.CharField(max_length=50, choices=OPTIONS)

    def __str__(self):
        return self.department
