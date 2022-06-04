from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from account.models import User, Student
from course.models import Course, Lesson
from evaluate.models import Evaluation
from evaluate.serializers import EvaluationSerializer


class EvaluateDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get_lesson(self, pk):
        try:
            return Lesson.objects.get(pk=pk)
        except Lesson.DoesNotExist:
            raise Http404

    def get_student(self, request):
        try:
            token_user = Token.objects.get(key=request.auth.key)
        except:
            return Response({'Message': 'The Token is not valid'},
                            status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(id=token_user.user.pk)
        try:
            student = Student.objects.get(user=user.pk)
        except:
            return Response({'Message': 'The User is not student'},
                            status=status.HTTP_400_BAD_REQUEST)
        return student

    def get(self, request, pk_course, pk_lesson):
        course = self.get_course(pk_course)
        student = self.get_student(request=request)
        lesson = self.get_lesson(pk_lesson)
        check_student_in_course = course.students.filter(pk=student.pk)
        check_student_in_lesson = lesson.students.filter(pk=student.pk)
        if check_student_in_course and check_student_in_lesson:
            evaluation = Evaluation.objects.get_or_create(lesson=lesson, student=student)
            serializer = EvaluationSerializer(evaluation[0])
            return Response(serializer.data)

        else:
            return Response({'Message': 'The student not found in course or lesson'},
                            status=status.HTTP_400_BAD_REQUEST)
