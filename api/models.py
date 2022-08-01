from django.db import models


class Entry(models.Model):
    date = models.DateTimeField()
    weight = models.FloatField()
    delta = models.FloatField()
    notes = models.CharField(max_length=500)
