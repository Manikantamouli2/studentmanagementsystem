from django.shortcuts import render
from .models import Student 
from django.http import HttpResponseRedirect
from django.http  import HttpResponse
from .forms import StudentRegistration,SignUpForm
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request,"crud/home.html")

@login_required
def list_student(request):
    student=Student.objects.all()
    return render(request,"crud/list_student.html",{"student":student})
def update(request,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=student)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm=StudentRegistration()
    return render(request,"crud/update.html",{"form":fm})

def add(request):
    if request.method=="POST":
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect("/")
    else:
        fm=StudentRegistration()
    
    return render(request,"crud/add.html",{"form":fm})
def delete(request,id):
    if request.method=="POST":
        student=Student.objects.get(pk=id)
        student.delete()
        return HttpResponseRedirect("/")
def searchstudent(request):
    if request.method == 'POST':
        n1 = request.POST.get('output')
        print(n1)
        student = Student.objects.all()
        std = None  # Initialize the variable
        if n1:
            std = student.filter(
                Q(fname__icontains=n1) |
                Q(lname__icontains=n1) |
                Q(email__icontains=n1) |
                Q(phone__icontains=n1) |
                Q(branch__icontains=n1)
            )
            print( std.count())
        return render(request, "crud/list_student.html", {'student': std})
    else:
        return HttpResponse('An Exception Occurred')
def signup_user(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/")
        else:
            form=SignUpForm()
        return render(request,'crud/signup.html',{'form':form})
    else:
        return HttpResponseRedirect("/")
def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                messages.success(request,"Congratulations!  You have successfully logged in." )
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/show')
        else:
            form = AuthenticationForm()
    else:
        return HttpResponseRedirect('/')

    
    return render(request, 'crud/login.html', {'form': form})

        





    




    

