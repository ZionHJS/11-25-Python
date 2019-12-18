from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, DailyReport, Clock, Quote
import bcrypt
from datetime import datetime
from decimal import Decimal

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
        User.objects.create(email=email, first_name=first_name,
                            last_name=last_name, password=user_pwd)
        request.session['this_user_id'] = this_user.id
        first_user = User.objects.first()
        first_user.user_level = 9
        first_user.save()
        messages.success(request, "Register successfully!")
        return redirect('/clockinout')


def clockinout(request):  # unfinished
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    user_clocks = this_user.clocks.all()
    clock_hours = 0
    clock_points = 0
    total_points = 0
    for clock in user_clocks:
        if clock.clockin is not None and clock.clockout is not None:  # judgement statement
            time1 = clock.clockin
            time2 = clock.clockout
            time_delta = time2-time1
            total_secondes = int(time_delta.total_seconds())
            clock_hours = total_secondes/3600
            clock.clock_hours = clock_hours
            clock_points = clock_hours*this_user.points_rate
            clock.clock_points = clock_points
            clock.save()
            total_points += clock_points
        else:
            clock_points = 0
    print("Total_Points:", total_points)
    this_user.total_points = total_points
    this_user.save()

    all_users_points = float(0)
    all_users = User.objects.all()
    for user in all_users:
        all_users_points += user.total_points
        # print(user)
        # print(all_users_points)

    random_quote = Quote.objects.order_by("?").first()

    clocks = Clock.objects.all().order_by('-created_at')
    last_clock = Clock.objects.last()
    context = {
        "this_user": this_user,
        "random_quote": random_quote,
        "this_user_points": this_user.total_points,
        "all_users_points": all_users_points,
        "clocks": clocks,
        "last_clock": last_clock,
        "date_cur": datetime.now()
    }
    return render(request, 'clockinout.html', context)


def clockout_yesterday(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    last_clock = Clock.objects.all().last()
    if not last_clock.clockout:
        last_clock.clockout = request.POST['clock_out']
        last_clock.task_des = request.POST['task_des']
        last_clock.save()
        return redirect('clockinout')
    else:
        return redirect('clockinout')


def points_test(request):
    all_users_points = 0
    all_users = User.objects.all()

    for user in all_users:
        all_users_points += user.total_points
        print('USER POINTS RATE', user.points_rate)
        print('USER POINTS TEST', all_users_points)
    return render(request, 'clockinout.html')


def clockin(request):  # works
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    new_clock = Clock.objects.create(
        user=this_user, clockin=datetime.now())
    return redirect('/clockinout')


def clockout(request):
    last_clock = Clock.objects.all().last()
    cur_date = datetime.now()
    if last_clock.clockin.date() == cur_date.date():
        task_des = request.POST['task_des']
        if not task_des:
            messages.error(request, 'Must Provide Task Description')
            return redirect('/clockinout')
        if not last_clock.clockin:
            return redirect('/clockinout')
        else:
            this_id = request.session.get('this_user_id')
            this_user = User.objects.get(id=this_id)
            last_clock.clockout = datetime.now()
            last_clock.task_des = task_des
            last_clock.save()
            return redirect('/clockinout')
    else:
        return redirect('/')
