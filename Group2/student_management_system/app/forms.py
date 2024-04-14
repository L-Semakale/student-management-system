from django import forms
from .models import Student, Teacher

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study']
        labels = {
            'student_number': 'Student Number',
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email',
            'field_of_study': 'Field of Study',
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
        }

class TeacherForm(forms.ModelForm):
<<<<<<< HEAD
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'email', 'password', 'faculty', 'is_teacher']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'faculty': forms.TextInput(attrs={'class': 'form-control'}),
            'is_teacher': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
=======
  class Meta:
    model = Teacher
    fields = ['first_name', 'last_name', 'email', 'password','faculty']
    labels = {
      'first_name': 'First Name',
      'last_name': 'Last Name',
      'email': 'Email',
      'password':'Password',
      'faculty': 'Faculty',
      
    }
    widgets = {
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'password': forms.PasswordInput(attrs={'class': 'form-control'}),
      'faculty': forms.TextInput(attrs={'class': 'form-control'}),
      
    }
>>>>>>> 51cea71165cb3f2e9f95167d9240da7090c92535

