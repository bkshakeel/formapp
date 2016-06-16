from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.template.context_processors import csrf



def login(request):
    c = {}
    c.update(csrf(request))
    return render(request,'login.html',c)

def signup(request):
    c = {}
    c.update(csrf(request))
    return render(request,'signup.html',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username,password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/frmexp/create')
    else:
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render(request,'loggedin.html',{'fullname':request.user.username})

def invalid_login(request):
    return render(request,'invalid.html')

def logout(request):
    return render(request,'logout.html')


def index(request):
    return render(request,'index.html',)
