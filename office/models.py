from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator # 유효성 검사

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(120)])
    heartrate = models.IntegerField(default = 60, validators = [MinValueValidator(1), MaxValueValidator(300)])

    def __str__(self):
        return f"{self.last_name} {self.first_name} is {self.age} years old!"