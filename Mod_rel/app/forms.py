from django import forms
from django.db import models
from django.forms import fields, widgets
from.models import Department,Student,Lecture


class StudentModel(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class LectureModel(forms.ModelForm):
    class Meta:
        model=Lecture
        fields='__all__'
        widgets={
            'Department':forms.CheckboxSelectMultiple()
        }
      




