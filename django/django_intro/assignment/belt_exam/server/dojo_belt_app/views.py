from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Wish
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register_verify(request):
    errors = User.objects.basic_validator_user(request.POST)
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
        first_user = User.objects.first()
        first_user.user_level = 9
        messages.success(request, "Register successfully!")
        return redirect('/dashboard')

def login_verify(request):
    found_user = User.objects.filter(email=request.POST['email'])
    if len(found_user) < 1:
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    else:
        logged_user = found_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['this_user_id'] = logged_user.id
            messages.success(request, "Successfully Logg-In")
            return redirect('/wishes')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')

def wishes(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    return render(request, 'wishes.html')
