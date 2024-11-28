from django import forms
from django.forms import ModelForm
from academic.models import Employee

class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        min_length=5,
        label='Enter Your Name',
        widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter name'})
        )
    age = forms.IntegerField(
        min_value=10,
        max_value=150,
        label='Enter age',
        widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'enter age'})
    )
    email = forms.EmailField(
        label='Enter email',
        widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'enter email'})
    )
    
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'