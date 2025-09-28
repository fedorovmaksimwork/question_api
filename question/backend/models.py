from django.db import models


class Question(models.Model):
    text = models.TextField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=False)

class Answer(models.Model):
    question_id = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE, editable=False)
    user_id = models.CharField(max_length=50, null=False, blank=False, editable=False)
    text = models.CharField(max_length=300, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, editable=False)



