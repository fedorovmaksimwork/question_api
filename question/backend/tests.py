import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Question, Answer


@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_create_question(api_client):
    data = {'text': 'Вопрос'}
    response = api_client.post(reverse('questions'), data=data)
    assert response.status_code == 201
    assert Question.objects.count() == 1

@pytest.mark.django_db
def test_get_all_questions(api_client):
    Question.objects.create(text='Вопрос1')
    Question.objects.create(text='Вопрос2')
    response = api_client.get(reverse('questions'))
    assert response.status_code == 200
    assert len(response.data) == 2

@pytest.mark.django_db
def test_get_single_question_and_answers(api_client):
    question = Question.objects.create(text='Вопрос')
    Answer.objects.create(question_id=question, user_id='test1', text='Ответ1')
    Answer.objects.create(question_id=question, user_id='test2', text='Ответ2')
    response = api_client.get(reverse('question', kwargs={'id': question.id}))
    assert response.status_code == 200
    assert len(response.data) == 3

@pytest.mark.django_db
def test_delete_question_cascade(api_client):
    question = Question.objects.create(text='Вопрос')
    Answer.objects.create(question_id=question, user_id='test', text='Ответ')
    response = api_client.delete(reverse('question', kwargs={'id': question.id}))
    assert response.status_code == 204
    assert Question.objects.count() == 0
    assert Answer.objects.count() == 0

@pytest.mark.django_db
def test_add_answer(api_client):
    question = Question.objects.create(text='Вопрос')
    data = {'text': 'Ответ', 'user_id':'test'}
    response = api_client.post(
        reverse('create_answer', kwargs={'id': question.id}),
        data=data,
        format='json'
    )
    assert response.status_code == 201
    assert Answer.objects.filter(question_id=question).count() == 1

@pytest.mark.django_db
def test_delete_answer(api_client):
    question = Question.objects.create(text='Вопрос')
    answer = Answer.objects.create(question_id=question, user_id='test', text='Ответ')
    response = api_client.delete(reverse('answer', kwargs={'id': answer.id}))
    assert response.status_code == 204
    assert Answer.objects.filter(pk=answer.id).exists() is False