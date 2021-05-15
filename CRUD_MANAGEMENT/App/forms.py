from django.forms import ModelForm, widgets
from django import forms
from .models import *


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'Rollno': forms.TextInput(attrs={'class': 'form-control'}),
            'phoneNum': forms.TextInput(attrs={'class': 'form-control'}),

        }




class MarkForm(ModelForm):

    class Meta:
        model = Marks
        fields = '__all__'

        widgets = {
            'studentName': forms.Select(attrs={'class': 'form-control'}),
            'operatingSystems': forms.TextInput(attrs={'class': 'form-control'}),
            'computerNetworks': forms.TextInput(attrs={'class': 'form-control'}),
            'DBMS': forms.TextInput(attrs={'class': 'form-control'}),
            'SWE': forms.TextInput(attrs={'class': 'form-control'}),
            'stats': forms.TextInput(attrs={'class': 'form-control'}),
            'LinearAlgebra': forms.TextInput(attrs={'class': 'form-control'}),
        }
