from django.http import Http404
from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User, Student
from course.models import Course, Lesson, StudentProgressInLesson
from course.serializers import CourseSerializer, CourseLessonsSerializer, LessonSerializer, LessonsSerializer


class CourseList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request):
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

        course_student = Course.objects.filter(students=student.pk)
        if course_student:
            serializer = CourseSerializer(course_student, many=True)
            return Response({'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'data': "The student dont have any course"}, status=status.HTTP_200_OK)


class CourseDetail(APIView):
    """
      Retrieve, update or delete a snippet instance.
      """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
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

    def put(self, request, pk):
        course = self.get_course(pk)
        student = self.get_student(request=request)
        check_student_in_course = course.students.filter(pk=student.pk)
        if check_student_in_course:
            return Response({'Message': 'The student already in this course'},
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            course.students.add(student.pk)
            serializer = CourseLessonsSerializer(course)
            return Response({'Message': 'ok register', 'data': serializer.data},
                            status=status.HTTP_200_OK)

    def delete(self, request, pk):
        course = self.get_course(pk)
        student = self.get_student(request=request)
        check_student_in_course = course.students.filter(pk=student.pk)
        if check_student_in_course:
            course.students.remove(student.pk)
            return Response({'Message': 'the student remove form this course'}, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'The student in not include in this course'},
                            status=status.HTTP_400_BAD_REQUEST)


class LessonList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_course(self, pk_course):
        try:
            return Course.objects.get(pk=pk_course)
        except Course.DoesNotExist:
            raise Http404

    def get_lessons(self, pk_course):
        try:
            return Lesson.objects.filter(course_id=pk_course)
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

    def get(self, request, pk):
        course = self.get_course(pk)
        student = self.get_student(request=request)
        check_student_in_course = course.students.filter(pk=student.pk)
        if check_student_in_course:
            lessons = self.get_lessons(pk)
            serializer = LessonsSerializer(lessons, many=True)
            return Response(serializer.data)
        else:
            return Response({'Message': 'The student in not include in this course'},
                            status=status.HTTP_400_BAD_REQUEST)


class LessonDetail(APIView):
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

    def get_lessons(self, pk_course):
        try:
            return Lesson.objects.filter(course_id=pk_course)
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
        i = 0
        prv_lesson = None
        check_student_in_course = course.students.filter(pk=student.pk)
        if check_student_in_course:
            lessons = self.get_lessons(pk_course)
            for itr_lesson in lessons:
                if lesson == itr_lesson:
                    if i != 0:
                        prv_lesson = lessons[i - 1]
                i += 1

            if prv_lesson is None or StudentProgressInLesson.objects.get(lesson=prv_lesson,
                                                                         student_id=student.pk).is_completed:
                lesson.students.add(student.pk)
                if lesson.course == course:
                    serializer = LessonSerializer(lesson)
                    return Response(serializer.data)
                else:
                    return Response({'Message': 'The lesson in not include in this course'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'Message': 'The Last lesson in not completed'},
                                status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({'Message': 'The student in not include in this course'},
                            status=status.HTTP_400_BAD_REQUEST)
