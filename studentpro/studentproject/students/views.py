from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/list.html', {'students': students})

def add_student(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        course = request.POST.get('course')

        Student.objects.create(
            name=name,
            age=age,
            email=email,
            course=course
        )
        return redirect('student_list')

    return render(request, 'students/add.html')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        student.save()
        return redirect('student_list')

    return render(request, 'students/edit.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.delete()
        return redirect('student_list')

    return render(request, 'students/delete.html', {'student': student})
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test

def superuser_check(user):
    return user.is_superuser

def superuser_login(request):
    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user and user.is_superuser:
            login(request, user)
            return redirect('/admin/')
        else:
            error = "Access denied! Superuser only."

    return render(request, 'students/superuser_login.html', {'error': error})
