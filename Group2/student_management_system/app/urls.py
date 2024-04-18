from django.urls import path
from . import views
from . import admin

urlpatterns = [
    path('index',views.index,name='index'),
    path('add',views.add,name='add'),
    path('',views.loginPage,name='login'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('details/<int:pk>',views.details,name='details'),
    path('view_student/<int:id>',views.view_student,name='view_student'),
    path('teacher',views.teacherForm,name='teacher'),
    path('logout',views.loginPage,name='logout')
]
