from django.db import models
from django.utils import timezone
# Create your models here.

class BMI(models.Model):
    name = models.CharField(max_length=200)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)

    date = models.DateTimeField(
            default=timezone.now)