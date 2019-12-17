from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, DailyReport, Clock, Quote
import bcrypt
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    request.session.clear()
    return redirect('/')

def register(request):
    return render(request, 'register.html')

def login_verify(request):
    found_user = User.objects.filter(email=request.POST['email'])
    if len(found_user) < 1:
        messages.error(request, 'Invalid Credentials')
        return redirect('/login')
    else:
        logged_user = found_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['this_user_id'] = logged_user.id
            return redirect('/clockinout')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/login')

def register_verify(request):
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
        User.objects.create(email=email, first_name=first_name, last_name=last_name, password=user_pwd)
        request.session['this_user_id'] = this_user.id
        first_user = User.objects.first()
        first_user.user_level = 9
        first_user.save()
        messages.success(request, "Register successfully!")
        return redirect('/clockinout')

def clockinout(request):   #unfinished
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    user_clocks = this_user.clocks.all()
    total_points = 0 
    for clock in user_clocks:
        clock_hour = clockout - clockin
        clock_points = clock_hour*this_user.points_rate
        total_points += clock_points
    this_user.total_points = total_points
    this_user.save()

    allusers_points = 0
    allusers = User.objects.all()
    for user in allusers:
        allusers_points += user.total_points
    
    random_quote = Quote.objects.order_by("?").first()

    clocks = Clock.object.all()
    context={
        "this_user":this_user,
        "random_quote":random_quote,
        "this_user_points":this_user.total_points,
        "allusers_points":allusers_points,
        "clocks":clocks
    }
    return render(request, 'clockinout.html', context)

def clockin(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    print('Now-Time:', datetime.datetime.now())
    new_clock = Clock.objects.create(user=this_user, clockin = datetime.datetime.now())
    return redirect('/clockinout')

def clockout(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    print('Now-Time:', datetime.datetime.now())
    last_clock = Clock.object.all().last()
    last_clock.clockout = datetime.datetime.now()
    return redirect('/clockinout')
