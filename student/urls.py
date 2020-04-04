from django.urls import path

from student import views

urlpatterns = [
    path("student_list/", views.student_list, name="student_list"),
    path("get_student/", views.get_student, name="get_student"),
    path("get_grade/", views.get_grade,name="get_grade"),
    path("edit_student/", views.edit_student,name="edit_student"),
]
