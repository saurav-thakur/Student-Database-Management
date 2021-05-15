from django.db import models
from django.db.models.deletion import SET_DEFAULT, SET_NULL
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=254, null=False, unique=True)
    Rollno = models.IntegerField(unique=True)
    phoneNum = PhoneNumberField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Marks(models.Model):
    studentName = models.ForeignKey(
        Student, null=True, on_delete=models.CASCADE, unique=True)
    # RollNumber = models.ForeignKey(
    #     Student.Rollno, null=True, on_delete=models.CASCADE)
    operatingSystems = models.FloatField(null=False)
    computerNetworks = models.FloatField(null=False)
    DBMS = models.FloatField(null=False)
    SWE = models.FloatField(null=False)
    stats = models.FloatField(null=False)
    LinearAlgebra = models.FloatField(null=False)

    def __str__(self):
        return self.studentName.name
