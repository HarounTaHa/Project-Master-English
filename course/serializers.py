from rest_framework import serializers

from account.serializers import StudentSerializer
from .models import Course, Lesson, WarmUp, StudentProgressInLesson, WarmUpQuestion, WarmUpAnswer


class CourseSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ['id', 'department', 'course_name', 'number_of_lessons']
        depth = 1


class WarmUpAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarmUpAnswer
        fields = ['text', 'correct']


class WarmUpQuestionSerializer(serializers.ModelSerializer):
    choices = serializers.SerializerMethodField('_get_choices')

    def _get_choices(self, WarmUpQuestion_object):
        pk_warm_up_question = getattr(WarmUpQuestion_object, 'id')
        try:
            warm_up_choices = WarmUpAnswer.objects.filter(question=pk_warm_up_question)
            return WarmUpAnswerSerializer(warm_up_choices, many=True).data
        except:
            return 'Not fount choices'

    class Meta:
        model = WarmUpQuestion
        fields = ['id', 'question', 'choices']


class WarmUpSerializer(serializers.ModelSerializer):
    question = serializers.SerializerMethodField('_get_question')

    def _get_question(self, WarmUp_object):
        pk_warm_up = getattr(WarmUp_object, 'id')
        try:
            warm_up_question = WarmUpQuestion.objects.get(warm_up=pk_warm_up)
            return WarmUpQuestionSerializer(warm_up_question).data
        except:
            return 'Not fount question'

    class Meta:
        model = WarmUp
        fields = ['id', 'warm_up', 'question']


class LessonSerializer(serializers.ModelSerializer):
    warm = serializers.SerializerMethodField('_get_warm')

    def _get_warm(self, lesson_object):
        pk_lesson = getattr(lesson_object, 'id')

        try:
            warm_up = WarmUp.objects.get(lesson=pk_lesson)
            return WarmUpSerializer(warm_up).data
        except:
            return 'Not found warm'

    class Meta:
        model = Lesson
        fields = ['id', 'objective', 'course', 'content', 'warm']


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'objective', 'course', 'content']


class CourseLessonsSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField('_get_lessons')

    def _get_lessons(self, course_object):
        pk_course = getattr(course_object, 'id')
        lessons = Lesson.objects.filter(course_id=pk_course)
        return LessonSerializer(lessons, many=True).data

    class Meta:
        model = Course
        fields = ['id', 'department', 'course_name', 'number_of_lessons', 'lessons']
