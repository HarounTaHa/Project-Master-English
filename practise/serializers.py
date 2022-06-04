from rest_framework import serializers

from .models import PractiseQuestionOne, AnswerQuestionOne, AnswerQuestionTwo, PractiseQuestionTwo
from .views import Practise


class AnswerQuestionOneSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestionOne
        fields = '__all__'


class PractiseQuestionOneSerializer(serializers.ModelSerializer):
    answer_question_one = serializers.SerializerMethodField('_get_answer_question_one')

    def _get_answer_question_one(self, practise_object):
        pk_question = getattr(practise_object, 'id')
        try:
            answers_question_one = AnswerQuestionOne.objects.filter(question=pk_question)
            return AnswerQuestionOneSerializer(answers_question_one, many=True).data
        except:
            return 'Not found Answer Question One'

    class Meta:
        model = PractiseQuestionOne
        fields = ['id', 'question_one', 'answer_question_one']


class AnswerQuestionTwoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnswerQuestionTwo
        fields = '__all__'


class PractiseQuestionTwoSerializer(serializers.ModelSerializer):
    answer_question_two = serializers.SerializerMethodField('_get_answer_question_two')

    def _get_answer_question_two(self, practise_object):
        pk_question = getattr(practise_object, 'id')
        try:
            answers_question_two = AnswerQuestionTwo.objects.filter(question=pk_question)
            return AnswerQuestionTwoSerializer(answers_question_two, many=True).data
        except:
            return 'Not found Answer Question One'

    class Meta:
        model = PractiseQuestionTwo
        fields = ['id', 'question_two', 'answer_question_two']


class PractiseSerializer(serializers.ModelSerializer):
    question_one = serializers.SerializerMethodField('_get_question_one')

    question_two = serializers.SerializerMethodField('_get_question_two')

    def _get_question_one(self, practise_object):
        pk_practise = getattr(practise_object, 'id')
        try:
            question_one = PractiseQuestionOne.objects.filter(practise=pk_practise)
            return PractiseQuestionOneSerializer(question_one[0]).data
        except:
            return 'Not found Question One'

    def _get_question_two(self, practise_object):
        pk_practise = getattr(practise_object, 'id')
        try:
            question_two = PractiseQuestionTwo.objects.filter(practise=pk_practise)
            return PractiseQuestionTwoSerializer(question_two[0]).data
        except:
            return 'Not found Question One'

    class Meta:
        model = Practise
        fields = ['id', 'lesson', 'student', 'question_one', 'question_two']
