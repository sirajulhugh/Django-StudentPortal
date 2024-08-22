import os
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import login
from .models import Course, Student,Teacher
from django.contrib.auth.decorators import login_required
from urllib.parse import urlencode
from django.shortcuts import redirect
from django.urls import reverse



# Create your views here.

def loginpage(request):
    return render (request,'loginpage.html')

def signuppage(request):
    a=Course.objects.all()
    return render (request,'signuppage.html',{'courses':a})

def log(request):
    if request.method=='POST':
        username=request.POST['usname']
        password=request.POST['passd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_authenticated:
                if user.is_staff:
                    print('ok')
                    login(request,user)
                    request.session['user'] = user.username
                    return redirect('adminmod')
                else:
                    login(request,user)
                    auth.login(request,user)
                    request.session['user'] = user.username
                    return redirect('usermod',id=user.id)
        else:
            messages.info(request,'Invalid Username or Password')
            return redirect('loginpage')
    return render(request,'signuppage.html')

def add_details(request): 
    if(request.method=='POST'):
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        ag=request.POST['age']
        pwd=request.POST['password']
        cpwd=request.POST['cp']
        ph=request.POST['phone']
        ad=request.POST['address']
        course_id = request.POST['course']
        course = Course.objects.get(id=course_id)
        mail=request.POST['email']
        img=request.FILES.get('image')
        if pwd==cpwd:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'Username already exists')
                return redirect('signuppage')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,password=pwd,email=mail)
                user.save()
                u=User.objects.get(id=user.id)
                reg=Teacher(age=ag,phnoenumber=ph,images=img,user=u,address=ad,course=course)
                reg.save()
                return redirect('loginpage')
        else:
            messages.info(request,'Incorrect Password')
            return redirect('/')
    

def adminmod(request):
    if request.user.is_staff:
        return render(request,'adminmod.html')
    else:
        query_params = {'error': 'access_denied'}
        url = '{}?{}'.format(reverse('loginpage'), urlencode(query_params))
        return redirect(url)


def usermod(request,id):
    user=User.objects.get(id=id)
    if 'user' in request.session:
        return render (request,'usermod.html',{'user':user})
    else:
        query_params = {'error': 'access_denied'}
        url = '{}?{}'.format(reverse('loginpage'), urlencode(query_params))
        return redirect(url)
    

def lgout(request):
    auth.logout(request)
    return redirect ('loginpage')

def page1(request):
    return render (request,'page1.html')

def add_course(request):
    return render (request,'add_course.html')

def addcourse(request):
    if request.method == 'POST':
        name = request.POST['name']
        fee = request.POST['fee']
        Course.objects.create(name=name, fee=fee)
        return redirect('add_student')
    
def edit_user(request,id):
    user=User.objects.get(id=id)
    std=Teacher.objects.get(user=user)
    cou=Course.objects.all()
    return render(request,"edit_user.html",{'teacher':std,'course':cou,'user':user})

def update(request,id):
    if request.method == 'POST':
        user=User.objects.get(id=id)
        teacher=Teacher.objects.get(user=user)
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.username = request.POST['uname']
        user.email = request.POST['email']
        age = request.POST['age']
        ph = request.POST['phone']
        ad = request.POST['address']
        course_id = request.POST['course']
        course = Course.objects.get(id=course_id)
        course.save()
        img = request.FILES.get('image')

       # if request.POST['password'] == request.POST['cp']:
        if User.objects.filter(username=user.username).exclude(id=user.id).exists():
                    messages.info(request, 'Username already exists')
                    return redirect('edit_user',id=user.id)
        else:
                    
                    user.save()

                    teacher.age = age
                    teacher.phnoenumber = ph
                    teacher.address = ad
                    teacher.course = course
                    if img:
                        teacher.images = img
                    teacher.save()
        return redirect('card_teacher',id=user.id)
    
def card_teacher(request,id):
    user=User.objects.get(id=id)
    teacher=Teacher.objects.get(user=user)
    return render(request, 'card_teacher.html', {'teacher': teacher})


def add_student(request):
    a=Course.objects.all()
    return render(request,'add_student.html',{'courses':a})
    


def addstudent(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        date_of_join = request.POST['date_of_join']
        course_id = request.POST['course']
        course = Course.objects.get(id=course_id)
        #Student.objects.create(name=name, age=age, address=address, date_of_join=date_of_join, course=course)
        std=Student(name=name, age=age, address=address, date_of_join=date_of_join, course=course)
        std.save()
    return redirect('student_list')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


def edit_student(request,id):
    std=Student.objects.get(id=id)
    cou=Course.objects.all()
    return render(request,"edit_student.html",{'student':std,'course':cou})

def editstudent(request,id):
    if request.method == 'POST':
        std=Student.objects.get(id=id)
        std.name = request.POST['name']
        std.age = request.POST['age']
        std.address = request.POST['address']
        std.date_of_join = request.POST['date_of_join']
        cor=request.POST['course']
        cor1=Course.objects.get(id=cor)
        cor1.save()
        std.course=cor1
        std.save()
        return redirect('student_list')

def deletestudent(request,id):
    std=Student.objects.get(id=id)
    std.delete()
    return redirect('student_list')

def teacher_list(request):
    teachers=Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

def delteacher(request,id):
    user=User.objects.get(id=id)
    user.delete()
    return redirect('teacher_list')