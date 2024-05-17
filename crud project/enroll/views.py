from django.shortcuts import render,HttpResponseRedirect
from .forms import SignupForm 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from .forms import StudentRegistration
from .models import kashif


# signup view function
def sign_up(req):
    if req.method == 'POST':
     fm = SignupForm(req.POST)
     if fm.is_valid():
        fm.save()
        messages.success(req, 'Account Has Created Successfully')
    else:
     fm = SignupForm()
    return render(req, 'enroll/signup.html', {'form':fm})

# login view function
def user_login(req):
  if not req.user.is_authenticated:
    if req.method == 'POST':
        fm = AuthenticationForm(data = req.POST)
        if fm.is_valid():
         uname = fm.cleaned_data['username']
         upass = fm.cleaned_data['password']
         user = authenticate(username = uname, password = upass)
         if user is not None:
            login(req, user)
            messages.success(req, 'Logged in Successfully..')
            return HttpResponseRedirect('/show/')
    else:
        fm = AuthenticationForm()
    return render(req, 'enroll/userlogin.html', {'form':fm})
  else:
    return HttpResponseRedirect('/profile/')

# profile page 
def user_profile(req):
  if req.user.is_authenticated:
    return render(req, 'enroll/profile.html', {'name':req.user})
  else:
    return HttpResponseRedirect('/login/')

# Logout page 
def user_logout(req):
  logout(req)
  return HttpResponseRedirect('/login/')






#create your view here
def create_user(req):
    if req.method == 'POST':
     fm = StudentRegistration(req.POST)
     if fm.is_valid():
        fm.save()
        fm = StudentRegistration()
    else:
     fm = StudentRegistration()
    stud = kashif.objects.all()
    return render(req,'enroll/show.html',{'form':fm, 'stu':stud})


 # This function will update
def update_data(req, id):
  if req.method == 'POST':
    data = kashif.objects.get(pk = id)
    fm = StudentRegistration(req. POST, instance = data)
    if fm.is_valid():
      fm.save()
  else:
      data = kashif.objects.get(pk = id)
      fm = StudentRegistration(instance = data)
  return render(req,'enroll/update.html', {'form':fm})


# Delete Functio
def delete_data(req,id):
  if req.method == 'POST':
    data = kashif.objects.get(pk = id)
    data.delete()
    return HttpResponseRedirect('/')





