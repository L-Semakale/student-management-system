from django.db import models

# Create your models here.
class Major(models.Model):
    name = models.CharField(max_length=256)
    code = models.CharField(max_length=10)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name}({self.code})'

class Module(models.Model):
    name = models.CharField(max_length=256)
    course = models.ForeignKey(Major,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.course}'

    
class Student(models.Model):
   student_number = models.PositiveIntegerField(primary_key=True,auto_created=True,unique=True)
   first_name = models.CharField(max_length=256)
   last_name = models.CharField(max_length=256)
   email = models.EmailField(unique=True)
   field_of_study = models.ForeignKey(Major,on_delete=models.CASCADE,related_name='student')
   

   def __str__(self):
      return f'Student: {self.first_name} {self.last_name}'

class Grade(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    module_name = models.ForeignKey(Module,on_delete=models.CASCADE)
    grade = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.student.first_name} ({self.module_name}({self.grade}))'
