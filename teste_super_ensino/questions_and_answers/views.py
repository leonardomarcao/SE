from rest_framework import viewsets, mixins, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Question, QuestionAndAnswer
from .permissions import IsUserOrReadOnly
from .serializers import (
    QuestionAnsweredSerializer,
    QuestionSerializer,
    ResumeSerializer
)


class QuestionViewSet(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (IsUserOrReadOnly,)


class QuestionAndAnswerViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    queryset = QuestionAndAnswer.objects.all()
    serializer_class = QuestionAnsweredSerializer
    permission_classes = (IsUserOrReadOnly,)

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        queryset = QuestionAndAnswer.objects.all()
        student_id = self.request.query_params.get('student_id')
        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)
        return queryset


class ResumeViewSet(
    viewsets.ViewSet
):
    serializer_class = ResumeSerializer

    def get(self, request):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        student_id = self.request.GET.get('student_id')
        # get all questions and answers
        queryset = QuestionAndAnswer.objects.all()
        # calculate total hits
        if student_id is not None:
            total_hits = queryset.filter(student_id=student_id).filter(alternative_id__is_correct=True).count()
            total_errors = queryset.filter(student_id=student_id).filter(alternative_id__is_correct=False).count()
            percentage = (total_errors + total_hits) * 100 / total_hits
            return Response({
                'total_hits': total_hits,
                'total_errors': total_errors,
                'percentage': percentage
            }, status=status.HTTP_200_OK)
        else:
            Response('Inform a correct student_id', status=status.HTTP_400_BAD_REQUEST)
