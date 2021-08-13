from collections import namedtuple
from django.urls import path

from .views import *


urlpatterns = [
    path("", list, name="student-list"),
    path("create/", add_student, name="student-add"),
    path("update/<int:pk>/", update_student, name="student-update"),
    path("delete/<int:pk>/", delete_student, name="student-delete"),
    path("home/", home, name="home"),
    path("create_futbolchi/", create_futbolchi, name="klub-create"),
    path("update_fultbolchi/<int:pk>/", update_futbolchi, name="klub-update"),
    path("delete_futtbolchi/<int:pk>/", delete_futbolchi, name="klub-delete")
]