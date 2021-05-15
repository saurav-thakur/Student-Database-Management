from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("student_marks/", views.marks, name="marks"),
    path("update_student/<str:pk>", views.updateStudent, name="update_student"),
    path("delete_student/<str:pk>", views.deleteStudent, name="delete_student"),
    path("update_marks/<str:pk>", views.updateMarks, name="update_marks"),
    path("delete_marks/<str:pk>", views.deleteMarks, name="delete_marks"),

]
