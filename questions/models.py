from django.db import models
from quizes.models import Quiz


# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=200, verbose_name="Текст вопроса")
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    text = models.CharField(max_length=300, verbose_name="Текст ответа")
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Вопрос: {self.question.text}, ответ: {self.text}, правильно: {self.correct}"
