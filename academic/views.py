from django.shortcuts import render, redirect
from academic.models import Student
from django.contrib.auth.models import User
from academic.forms import *
from academic.utils import *
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def create_student(request):
    if request.method == 'POST':
        data = request.POST
        stdname = data.get('stdName')
        stdage = data.get('stdAge')
        stdemail = data.get('stdEmail')
        Student.objects.create(name=stdname, age=stdage, email=stdemail)
    return render(request, 'create-student.html')

@login_required(login_url='/login')
def get_students(request):
    data = Student.objects.values()
    return render(request, 'students.html', context={'students':data})


def delete_student(request,id):
    Student.objects.get(id=id).delete()
    return redirect('/students')

def update_student(request,id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        student.name = data.get('stdName')
        student.age = data.get('stdAge')
        student.email = data.get('stdEmail')
        student.save()
        return redirect('/students')
    return render(request, "update-student.html", context={'data': student})


def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            age = form.cleaned_data.get('age')
            email = form.cleaned_data.get('email')
            Student.objects.create(name=name, age=age, email=email)
            return redirect('/createstd')
    form = StudentForm()
    return render(request, 'student-form.html', context={'formdata':form})

def send_email_demo(request):
    if request.method == 'POST':
        data = request.POST
        rec_list = []
        subject = data.get('subject')
        body = data.get('body')
        rec = data.get('email')
        rec_list.append(rec)
        send_email_util(subject, body, rec_list)
        return redirect('/sendemail')
    return render(request, 'test.html')

def create_user(request):
    if request.method == 'POST':
        data = request.POST
        first_name = data.get('fname')
        last_name = data.get('lname')
        email = data.get('useremail')
        password = data.get('password')
        username = data.get('username')
        user = User(first_name=first_name, last_name=last_name, email=email, username=username)
        user.set_password(password)
        user.save()
        messages.success(request, 'user created')
        return redirect('/register')
    return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'invalid username')
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, 'invalid password')
            return redirect('/login')
        else:
            login(request, user)
            return redirect('/students')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('/login')