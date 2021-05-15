from django.shortcuts import redirect, render, HttpResponse

# Create your views here.

from .models import *
from .forms import *


def home(request):
    student = Student.objects.all()
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'student': student, 'form': form}

    return render(request, "App/home.html", context)


def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {'student': student, 'form': form}

    return render(request, 'App/update_student.html', context)


def marks(request):
    marks = Marks.objects.all()
    form = MarkForm()

    total_sum = 0

    if request.method == "POST":
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/student_marks/")


    context = {'marks': marks, 'form': form}

    return render(request, 'App/marks.html', context)


def deleteStudent(request, pk):
    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == "POST":
        student.delete()
        return redirect("/")

    context = {'student': student}

    return render(request, 'App/delete_student.html', context)


def updateMarks(request, pk):
    marks = Marks.objects.get(id=pk)
    form = MarkForm(instance=marks)

    if request.method == "POST":
        form = MarkForm(request.POST, instance=marks)
        if form.is_valid():
            form.save()
            return redirect('/student_marks/')

    context = {'marks': marks, 'form': form}
    return render(request, "App/update_marks.html", context)


def deleteMarks(request, pk):
    marks = Marks.objects.get(id=pk)
    form = MarkForm(instance=marks)

    if request.method == "POST":
        marks.delete()
        return redirect("/student_marks/")

    context = {'marks': marks, 'form': form}

    return render(request, 'App/delete_marks.html', context)
