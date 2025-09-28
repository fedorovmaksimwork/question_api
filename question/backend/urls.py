
from django.urls import path
from .views import QuestionListApiView, QuestionDetailApiView, AnswerCreateApiView, AnswerDetailApiView

urlpatterns = [
    path('questions/', QuestionListApiView.as_view(), name='questions'),
    path('questions/<int:id>/', QuestionDetailApiView.as_view(), name='question'),
    path('answers/<int:id>/', AnswerDetailApiView.as_view(), name='answer'),
    path('questions/<int:id>/answers/', AnswerCreateApiView.as_view(), name='create_answer')
]