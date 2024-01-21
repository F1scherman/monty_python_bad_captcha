from django.db import models

# Create your models here.


class CaptchaQuestion(models.Model):
    question_text: str
    correct_answer_pattern: str
