from django.urls import path

from .views import PractiseDetail

app_name = 'practise'

urlpatterns = [
    path('courses/<int:pk_course>/lessons/<int:pk_lesson>', PractiseDetail.as_view()),
]
