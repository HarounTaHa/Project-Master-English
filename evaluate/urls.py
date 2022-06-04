from django.urls import path

from .views import EvaluateDetail

app_name = 'evaluate'

urlpatterns = [
    path('courses/<int:pk_course>/lessons/<int:pk_lesson>', EvaluateDetail.as_view()),
]
