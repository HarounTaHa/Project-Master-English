from rest_framework import serializers

from evaluate.models import Evaluation, EvaluationAnswer, EvaluationQuestion


class EvaluationAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EvaluationAnswer
        fields = ['id', 'answer', 'is_correct']


class EvaluationQuestionSerializer(serializers.ModelSerializer):
    answers_questions = serializers.SerializerMethodField('_get_answers_questions')

    def _get_answers_questions(self, practise_object):
        pk_question = getattr(practise_object, 'id')
        try:
            answers_questions = EvaluationAnswer.objects.filter(evaluation_question=pk_question)
            return EvaluationAnswerSerializer(answers_questions, many=True).data
        except:
            return 'Not found Answer Question One'

    class Meta:
        model = EvaluationQuestion
        fields = ['id', 'question', 'answers_questions']


class EvaluationSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField('_get_questions')

    def _get_questions(self, practise_object):
        pk_evaluate = getattr(practise_object, 'id')
        try:
            questions = EvaluationQuestion.objects.filter(evaluation=pk_evaluate)
            return EvaluationQuestionSerializer(questions, many=True).data
        except:
            return 'Not found Questions'

    class Meta:
        model = Evaluation
        fields = ['id', 'instructions', 'student', 'revise', 'is_available', 'questions']
