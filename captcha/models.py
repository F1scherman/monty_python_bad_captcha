from django.db import models
import re

# Create your models here.


class CaptchaQuestion(models.Model):
    question_text = models.CharField(max_length=500)
    correct_answer_pattern = models.CharField(max_length=500)

    def __str__(self):
        return self.question_text + " -> " + self.correct_answer_pattern

    def check_correct_answer(self, candidate: str):
        if re.search(self.correct_answer_pattern, candidate) is not None:
            return True
        return False
