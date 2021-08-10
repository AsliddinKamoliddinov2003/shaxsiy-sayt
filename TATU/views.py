from django import forms
from django.urls.base import is_valid_path
from TATU.forms import StudentsForm
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import *
from .forms import *

def list(request):
    students = Students.objects.all()
    context = {
        "students":students
    }
    return render(request, "TATU/list.html", context)


def add_student(request):
    form = StudentsForm()
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("student-list"))


    context = {
        "form":form
    }

    return render(request, "TATU/create.html", context)


def update_student(request, pk):
    student = Students.objects.filter(id=pk)

    if not student.exists():
        return redirect(reverse("student-list"))
    else:
        student = student.first()

    form = StudentsForm(instance=student)
    if request.method == "POST":
        student = StudentsForm(request.POST, instance=student)
        if student.is_valid():
            student.save()
            return redirect(reverse("student-list"))

       
    context = {
        "form":form
    }
    return render(request, "TATU/update.html", context)


def delete_student(request, pk):

    try:
        student = Students.objects.get(id=pk)
        student.delete()
    except Direction.DoesNotExist:
        pass
    return redirect(reverse("student-list"))
    
