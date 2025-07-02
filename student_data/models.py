from django.db import models

MY_CHOICES = [
        ("CE", 'CE'),
        ("EXTC", 'EXTC'),
        ("ME", 'ME'),
        ("AI", 'AI'),
        ("IT", 'IT'),
    ]


class Student(models.Model):
    fname=models.CharField(max_length=25)
    lname=models.CharField(max_length=25)
    email=models.EmailField(max_length=25)
    phone=models.PositiveIntegerField()
    branch=models.CharField(max_length=50,choices=MY_CHOICES)

    def __str__(self):
        return self.fname