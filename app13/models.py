from django.db import models


class Ass13(models.Model):
    name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    cno = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=10)
    total = models.DecimalField(max_digits=10, decimal_places=2)
