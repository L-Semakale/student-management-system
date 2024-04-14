from django.contrib import admin
from .models import Student,Grade,Module,Major,Teacher

# Register your models here.,
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Module)
admin.site.register(Major)
admin.site.register(Teacher)