from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signin(request):
    return render(request, 'signin.html')

def logoff(request):
    request.session.clear()
    return redirect('/')

def register(request):
    return render(request, 'register.html')

def regisration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    elif request.POST['password_confirm'] != request.POST['password']:
        messages.error(request, 'The password entered twice must be the same!')
    else:
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        user_pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        this_user = User.objects.create(email=email, first_name=first_name, last_name=last_name, password=user_pwd)
        request.session['this_user_id'] = this_user.id
        first_user = User.objects.get(id=1)
        first_user.user_level = 9
        messages.success(request, "Register successfully!")
        return redirect('/dashboard')

def dashboard(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    users = User.objects.all()
    if this_user is not None:
        context={
            "users":users,
            "admin_num":9
        }
        return render(request, 'user_dashboard.html', context)
    else:
        return redirect('/')

def edit_self(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    users = User.objects.all()
    if this_user is not None:
        context={
            "users":users,
            "this_user":this_user
        }
        return render(request, 'user_dashboard.html', context)
    else:
        return redirect('/')
    return render(request, 'edit_self.html')

