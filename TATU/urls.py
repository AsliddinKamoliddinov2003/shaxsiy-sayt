from django.urls import path

from .views import *


urlpatterns = [
    path("", list, name="student-list"),
    path("create/", add_student, name="student-add"),
    path("update/<int:pk>/", update_student, name="student-update"),
    path("delete/<int:pk>/", delete_student, name="student-delete")
]