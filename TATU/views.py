from django.shortcuts import redirect, render
from django.urls import reverse

from .models import *

def list(request):
    students = Students.objects.all()
    context = {
        "students":students
    }
    return render(request, "TATU/list.html", context)


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        surname = request.POST.get("surname", None)
        age = request.POST.get("age", None)
        phone = request.POST.get("phone", None)
        nation = request.POST.get("nation", None)
        direction_id = request.POST.get("direction_id", None)

        direction = Direction.objects.get(id=direction_id)

        s = Students()
        s.name = name
        s.surname = surname
        s.age = age
        s.phone = phone
        s.nation = nation
        s.direction = direction

        s.save()

        return redirect(reverse("student-list"))

    directions = Direction.objects.all()

    context = {
        "directions":directions
    }

    return render(request, "TATU/create.html", context)


def update_student(request, pk):
    student = Students.objects.filter(id=pk)

    if not student.exists():
        return redirect(reverse("student-list"))
    else:
        student = student.first()


    if request.method == "POST":
        name = request.POST.get("name", None)
        surname = request.POST.get("surname", None)
        age = request.POST.get("age", None)
        phone = request.POST.get("phone", None)
        nation = request.POST.get("nation", None)
        direction_id = request.POST.get("direction_id", None)

        direction = Direction.objects.get(id = direction_id)

        student.name = name
        student.surname = surname
        student.age = age
        student.phone = phone
        student.nation = nation
        student.direction = direction

        student.save()

        return redirect(reverse("student-list"))

    directions = Direction.objects.all()

    context = {
        "directions":directions,
        "student":student,

    }
    return render(request, "TATU/update.html", context)


def delete_student(request, pk):

    try:
        student = Students.objects.get(id=pk)
        student.delete()
    except Direction.DoesNotExist:
        pass
    return redirect(reverse("student-list"))
    
