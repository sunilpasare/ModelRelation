from django.http import request
from django.shortcuts import render,redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def userregister(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    template_name='register.html'
    context={'form':form}
    return render(request,template_name,context)

def userlogin(request):
   
    if request.method=='POST':
         u=request.POST.get('un')
         p=request.POST.get('pw')
         print(u,p)
         user=authenticate(username=u,password=p)

         if user is not None:
             print('valid credentials')
             print('actual Logincode')
             login(request,user)
             return redirect('home')
         else:
             print('valid credentials')
             messages.error(request,'invalid credentials')
    template_name='login.html'
    context={}
    return render(request,template_name,context)

def logoutview(request):
    logout(request)
    return redirect('login')


