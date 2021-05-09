from django.db import models
from simple_history.models import HistoricalRecords


# Create your models here.

class TestDocs(models.Model):
    name = models.CharField(max_length=200)
    document = models.FileField()
    history = HistoricalRecords()

    def __str__(self):
        return self.name
