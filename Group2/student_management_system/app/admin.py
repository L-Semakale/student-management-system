from django.contrib import admin
from .models import Student,Grade,Module,Major

# Register your models here.,
admin.site.register(Student)
admin.site.register(Grade)
admin.site.register(Module)
admin.site.register(Major)