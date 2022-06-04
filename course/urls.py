from django.urls import path

from .views import CourseList, CourseDetail, LessonList,LessonDetail

app_name = 'course'

urlpatterns = [
    path('', CourseList.as_view()),
    path('<int:pk>/', CourseDetail.as_view()),
    path('<int:pk>/lessons/', LessonList.as_view()),
    path('<int:pk_course>/lessons/<int:pk_lesson>/', LessonDetail.as_view()),
]
