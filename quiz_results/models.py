from django.db import models
from quizes.models import Quiz
from django.contrib.auth.models import User


# Create your models here.
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='quiz', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    score = models.FloatField()
    created = models.DateTimeField(auto_now_add=True, blank=True,)

    def __str__(self):
        return str(self.pk)
