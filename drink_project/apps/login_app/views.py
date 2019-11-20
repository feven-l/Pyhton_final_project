from django.shortcuts import render, HttpResponse, redirect
from .models import User, UserManager
from django.contrib import messages
import bcrypt


def index(request):
    if 'userid' in request.session:
        return redirect('/dashboard')
    return render(request, 'login_app/login.html')

def register(request):
    if 'userid' in request.session:
        return redirect('/dashboard')
    return render(request, 'login_app/index.html')

def reg_process(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:   
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        confirm_pw = request.POST['confirm_pw']
        confirmpw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        new_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], birthday=request.POST['birthday'], password=pw_hash, confirm_pw=confirmpw_hash)
        request.session['userid'] = new_user.id
        return redirect ('/dashboard')
def log_process(request):
    errors = User.objects.log_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:   
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id 
                return redirect ('/dashboard')
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
    