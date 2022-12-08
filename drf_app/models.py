from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(validators=[MinValueValidator(1000000000),
                                       MaxValueValidator(9999999999)])
    age = models.IntegerField()
    salary = models.IntegerField()
    dept = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

