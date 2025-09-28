from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpRequest, HttpResponse
from rest_framework import generics, status

from rest_framework.mixins import ListModelMixin, CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response

from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer

import uuid

class QuestionListApiView(ListModelMixin, CreateModelMixin, generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class QuestionDetailApiView(DestroyModelMixin, generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'id'

    def get(self, request: HttpRequest, id) -> HttpResponse:
        question = self.get_object()
        serializer = QuestionSerializer(question)
        data = {'question': serializer.data}
        answers = Answer.objects.filter(question_id__id=id)
        for i, answer in enumerate(answers):
            serializer = AnswerSerializer(answer)
            data[f'answer{i+1}'] = serializer.data
        return Response(data)

    def delete(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.destroy(request, *args, **kwargs)
        return Response({"status": "Question deleted"}, status=status.HTTP_204_NO_CONTENT)


class AnswerDetailApiView(DestroyModelMixin, generics.GenericAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = 'id'

    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        answer = Answer.objects.get(id=id)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data)

    def delete(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        self.destroy(request, *args, **kwargs)
        return Response({"status": "Question deleted"}, status=status.HTTP_204_NO_CONTENT)

class AnswerCreateApiView(generics.GenericAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    lookup_field = 'id'

    def post(self, request: HttpRequest, id: int, *args, **kwargs) -> HttpResponse:
        try:
            question = Question.objects.get(id=id)
        except ObjectDoesNotExist:
            return Response({"status": "Question is not detected"}, status=status.HTTP_404_NOT_FOUND)
        if 'id' not in request.session:
            request.session['id'] = str(uuid.uuid4())
        print(request.session['id'])
        data = request.data
        serializer = AnswerSerializer(data=data)
        if serializer.is_valid():
            answer = Answer.objects.create(question_id=question, user_id=request.session['id'], text=data['text'])
            answer.save()
            return Response({"status": "Answer created", "id": answer.id}, status=status.HTTP_201_CREATED)
        return Response({"status": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)


