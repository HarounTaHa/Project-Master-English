from django.contrib import admin
from .models import Evaluation,EvaluationQuestion,EvaluationAnswer
# Register your models here.
admin.site.register([Evaluation,EvaluationQuestion,EvaluationAnswer])