from TATU.forms import StudentsForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.db import transaction

from .models import *
from .forms import *
from .utils import *

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


def home(request):
    klubs = Klub.objects.all()
    context = {
        "klubs":klubs
    }

    return render(request, "TATU/home.html", context)

def create_futbolchi(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        state = request.POST.get("state",None)
        date = request.POST.get("date", None)
        time = request.POST.get("time", None)
        fullname = request.POST.get("fullname", None)
        age = request.POST.get("age", None)
        salary = request.POST.get("salary", None)
        
        with transaction.atomic():
            k = Klub(
                name = name,
                state = state,
                established_at = parse_date_time(date, time)
            )        
            k.save()

            f = Futbolchi(
                fullname = fullname,
                age = age,
                salary = salary,
                klub = k
                
            )
            f.save()

        return redirect(reverse("home"))

    context = {

    }

    return render(request, "TATU/create_futbolchi.html", context)


def update_futbolchi(request, pk):
    try:
        klub = Klub.objects.get(id=pk)
        date = klub.established_at.strftime("%Y-%m-%d")
        time = klub.established_at.strftime("%H:%M")
    except:
        return redirect(reverse("home"))
    
    if request.method == "POST":
        name = request.POST.get("name", None)
        state = request.POST.get("state",None)
        date = request.POST.get("date", None)
        time = request.POST.get("time", None)
        fullname = request.POST.get("fullname", None)
        age = request.POST.get("age", None)
        salary = request.POST.get("salary", None)
        
        klub.name = name
        klub.state = state
        klub.established_at = parse_date_time(date, time)
        klub.futbolchi.fullname = fullname
        klub.futbolchi.age = age
        klub.futbolchi.salary = salary
        klub.save()
        klub.futbolchi.save()
        

        return redirect(reverse("home"))

    context = {
        "klub":klub,
        "date":date,
        "time":time
    }
    return render(request, "TATU/update_futbolchi.html", context)



def delete_futbolchi(request, pk):
    try:
        Klub.objects.get(id=pk).delete()
    except:
        pass
    return redirect(reverse("home"))


    
    
