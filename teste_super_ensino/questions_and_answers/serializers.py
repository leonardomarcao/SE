from rest_framework import serializers
from .models import Question, QuestionAndAnswer


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("name", "text")


class QuestionAnsweredSerializer(serializers.ModelSerializer):
    question = serializers.CharField(source="question_id.text", label="Questão")
    answered_alternative = serializers.CharField(
        source="alternative_id.text", label="Alternative respondida"
    )
    is_correct = serializers.BooleanField(
        source="alternative_id.is_correct", label="É correta?"
    )

    class Meta:
        model = QuestionAndAnswer
        fields = ("question", "answered_alternative", "is_correct", "answered_time")


class ResumeSerializer(serializers.ModelSerializer):
    total_hits = serializers.FloatField()
    total_errors = serializers.FloatField()
    percentage = serializers.FloatField()
