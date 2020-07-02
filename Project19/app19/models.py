from django.db import models


class EmpolyeeModel(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    doj=models.DateField()
