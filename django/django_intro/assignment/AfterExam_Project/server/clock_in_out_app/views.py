from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
from datetime import datetime, timedelta
from decimal import Decimal
from random import choice
from queue import Queue

# Views


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


def daily_quote():
    all_quotes = Quote.objects.all()
    quote_list = []
    for quote in all_quotes:
        quote_list.append(quote)
    last_quote = quote_list[-1]
    cur_date = datetime.now()
    if last_quote.updated_at.date() == cur_date.date():
        today_quote = last_quote
    elif last_quote.updated_at.date() < cur_date.date():
        today_quote = quote_list.pop(0)
        today_quote.updated_at = cur_date
        today_quote.save()
        quote_list.append(today_quote)
    return today_quote


def clockinout(request):  # unfinished
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id:  # check login
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
                clock_hours = round(total_secondes/3600, 3)
                clock.clock_hours = clock_hours
                clock_points = round(clock_hours*this_user.points_rate, 3)
                clock.clock_points = clock_points
                clock.save()
                total_points += clock_points
            else:
                clock_points = 0
        this_user.total_points = total_points
        this_user.save()

        all_users_points = float(0.01)
        all_users = User.objects.all()
        for user in all_users:
            all_users_points += round(user.total_points, 2)

        today_quote = daily_quote()

        clocks = Clock.objects.all().order_by('-created_at')
        last_clock = Clock.objects.last()
        last_clockout_choice = last_clock.clockin.replace(
            tzinfo=None)  # remove the timezone

        last_clockout_choice = last_clock.clockin

        lastclock_midnight_time = last_clockout_choice.replace(
            hour=23, minute=59, second=59, microsecond=0)

        last_clockout_choices = []

        while last_clockout_choice < lastclock_midnight_time:
            last_clockout_choices.append(last_clockout_choice)
            last_clockout_choice += timedelta(minutes=30)

        if request.session['show_employee_id']:
            show_employee_id = request.session['show_employee_id']
            show_employee = User.objects.get(id=show_employee_id)
        else:
            shiw_employee = {}

        context = {
            "this_user": this_user,
            "employees": User.objects.all(),
            "show_employee": show_employee,
            "today_quote": today_quote,
            "this_user_points": round(this_user.total_points, 2),
            "all_users_points": all_users_points,
            "clocks": clocks,
            "last_clock": last_clock,
            "date_cur": datetime.now().strftime("%H:%M %p. | %d-%M-%Y "),
            "last_clockout_choices": last_clockout_choices
        }
        return render(request, 'clockinout.html', context)
    else:
        return redirect('/')


def get_employee(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id:
        show_employee_id = request.POST['employee_id']
        request.session['show_employee_id'] = show_employee_id
        return redirect('/clockinout')
    else:
        return redirect('/')


def clockout_lasttime(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    last_clock = Clock.objects.all().last()
    if this_id:  # check login
        if not last_clock.clockout:
            if request.POST['task_des']:
                last_clock.clockout = datetime.strptime(
                    request.POST['clock_out'], "%Y-%m-%d %H:%M")
                last_clock.task_des = request.POST['task_des']
                last_clock.save()
                return redirect('/clockinout')
            else:
                messages.error(
                    request, 'Must Provide Task Description')
                return redirect('/')
        else:
            messages.error(
                request, 'The last clockout is finished or the last clockin is in the same-day, please use clockout button for today or just clockin!')
            return redirect('/clockinout')
    else:
        return redirect('/')


def clockin(request):  # works
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id:  # check login
        new_clock = Clock.objects.create(
            user=this_user, clockin=datetime.now())
        return redirect('/clockinout')
    else:
        return redirect('/')


def clockout(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id:  # check login
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
            messages.error(
                request, 'the clockout time is not today, please check "forgot to clock out yesterday"')
            return redirect('/clockinout')
    else:
        return redirect('/')


def points(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id:
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
                clock_hours = round(total_secondes/3600, 3)
                clock.clock_hours = clock_hours
                clock_points = round(clock_hours*this_user.points_rate, 3)
                clock.clock_points = clock_points
                clock.save()
                total_points += clock_points
            else:
                clock_points = 0
        this_user.total_points = total_points
        this_user.save()

        all_users_points = float(0.01)
        all_users = User.objects.all()
        for user in all_users:
            all_users_points += round(user.total_points, 2)

        today_quote = daily_quote()
        clocks = Clock.objects.all().order_by('-created_at')
        last_clock = Clock.objects.last()

        last_clockout_choice = last_clock.clockin.replace(
            tzinfo=None)  # remove the timezone

        last_clockout_choice = last_clock.clockin

        lastclock_midnight_time = last_clockout_choice.replace(
            hour=23, minute=59, second=59, microsecond=0)

        last_clockout_choices = []

        while last_clockout_choice < lastclock_midnight_time:
            last_clockout_choices.append(last_clockout_choice)
            last_clockout_choice += timedelta(minutes=30)

        context = {
            "this_user": this_user,
            "today_quote": today_quote,
            "this_user_points": round(this_user.total_points, 2),
            "all_users_points": all_users_points,
            "clocks": clocks,
            "last_clock": last_clock,
            "date_cur": datetime.now().strftime("%H:%M %p. | %d-%M-%Y "),
            "last_clockout_choices": last_clockout_choices
        }
        return render(request, 'points.html', context)
    else:
        return redirect('/')


def report(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id:
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
                clock_hours = round(total_secondes/3600, 3)
                clock.clock_hours = clock_hours
                clock_points = round(clock_hours*this_user.points_rate, 3)
                clock.clock_points = clock_points
                clock.save()
                total_points += clock_points
            else:
                clock_points = 0
        this_user.total_points = total_points
        this_user.save()

        all_users_points = float(0.01)
        all_users = User.objects.all()
        for user in all_users:
            all_users_points += round(user.total_points, 2)

        today_quote = daily_quote()
        clocks = Clock.objects.all().order_by('-created_at')
        last_clock = Clock.objects.last()

        last_clockout_choice = last_clock.clockin.replace(
            tzinfo=None)  # remove the timezone

        last_clockout_choice = last_clock.clockin

        lastclock_midnight_time = last_clockout_choice.replace(
            hour=23, minute=59, second=59, microsecond=0)

        last_clockout_choices = []

        while last_clockout_choice < lastclock_midnight_time:
            last_clockout_choices.append(last_clockout_choice)
            last_clockout_choice += timedelta(minutes=30)

        context = {
            "this_user": this_user,
            "today_quote": today_quote,
            "this_user_points": round(this_user.total_points, 2),
            "all_users_points": all_users_points,
            "clocks": clocks,
            "last_clock": last_clock,
            "date_cur": datetime.now().strftime("%H:%M %p. | %d-%M-%Y "),
            "last_clockout_choices": last_clockout_choices
        }
        return render(request, 'report.html', context)
    else:
        return redirect('/')


def report_verify(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id:
        cur_date = datetime.now()
        last_reports = DailyReport.objects.last()
        if not last_reports:
            recipients = request.POST['recipients']
            done = request.POST['done']
            challenges = request.POST['challenges']
            helps = request.POST['helps']
            user = this_user
            new_daily_report = DailyReport.objects.create(
                recipients=recipients, done=done, challenges=challenges, helps=helps, user=user)
            return redirect('/report')
        else:
            if last_reports.created_at.date() == cur_date.date():
                messages.error(
                    request, 'Can\'t report twice in a single-day!')
                return redirect('/report')
            else:
                recipients = request.POST['recipients']
                done = request.POST['done']
                challenges = request.POST['challenges']
                helps = request.POST['helps']
                user = this_user
                new_daily_report = DailyReport.objects.create(
                    recipients=recipients, done=done, challenges=challenges, helps=helps, user=user)
                return redirect('/report')
    else:
        return redirect('/')


def settings(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id:
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
                clock_hours = round(total_secondes/3600, 3)
                clock.clock_hours = clock_hours
                clock_points = round(clock_hours*this_user.points_rate, 3)
                clock.clock_points = clock_points
                clock.save()
                total_points += clock_points
            else:
                clock_points = 0
        this_user.total_points = total_points
        this_user.save()

        all_users_points = float(0.01)
        all_users = User.objects.all()
        for user in all_users:
            all_users_points += round(user.total_points, 2)

        today_quote = daily_quote()
        clocks = Clock.objects.all().order_by('-created_at')
        last_clock = Clock.objects.last()

        last_clockout_choice = last_clock.clockin.replace(
            tzinfo=None)  # remove the timezone

        last_clockout_choice = last_clock.clockin

        lastclock_midnight_time = last_clockout_choice.replace(
            hour=23, minute=59, second=59, microsecond=0)

        last_clockout_choices = []

        while last_clockout_choice < lastclock_midnight_time:
            last_clockout_choices.append(last_clockout_choice)
            last_clockout_choice += timedelta(minutes=30)

        context = {
            "this_user": this_user,
            "today_quote": today_quote,
            "this_user_points": round(this_user.total_points, 2),
            "all_users_points": all_users_points,
            # "clocks": clocks,
            "last_clock": last_clock,
            "date_cur": datetime.now().strftime("%H:%M %p. | %d-%M-%Y "),
            "last_clockout_choices": last_clockout_choices
        }
        return render(request, 'settings.html', context)
    else:
        return redirect('/')


def reset_password_verify(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id:
        if bcrypt.checkpw(request.POST['previous_password'].encode(), this_user.password.encode()):
            errors = User.objects.basic_validator_password(request.POST)
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/settings')
            elif request.POST['password_confirm'] != request.POST['password']:
                messages.error(
                    request, 'The password entered twice must be the same!')
                return redirect('/settings')
            else:
                new_password = request.POST['password']
                user_pwd = bcrypt.hashpw(
                    new_password.encode(), bcrypt.gensalt()).decode()
                this_user.password = user_pwd
                this_user.save()
                messages.success(request, "Reset Password Successfully!")
                return redirect('/settings')
        else:
            messages.error(
                request, 'Please Type in the Correct Previous-Password!')
            return redirect('/settings')
    else:
        return redirect('/')


def admin(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id and this_user.user_level == 9:  # check login
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
                clock_hours = round(total_secondes/3600, 3)
                clock.clock_hours = clock_hours
                clock_points = round(clock_hours*this_user.points_rate, 3)
                clock.clock_points = clock_points
                clock.save()
                total_points += clock_points
            else:
                clock_points = 0
        this_user.total_points = total_points
        this_user.save()

        all_users_points = float(0.01)
        all_users = User.objects.all()
        for user in all_users:
            all_users_points += round(user.total_points, 2)

        today_quote = daily_quote()

        clocks = Clock.objects.all().order_by('-created_at')
        last_clock = Clock.objects.last()
        last_clockout_choice = last_clock.clockin.replace(
            tzinfo=None)  # remove the timezone

        last_clockout_choice = last_clock.clockin

        lastclock_midnight_time = last_clockout_choice.replace(
            hour=23, minute=59, second=59, microsecond=0)

        last_clockout_choices = []

        while last_clockout_choice < lastclock_midnight_time:
            last_clockout_choices.append(last_clockout_choice)
            last_clockout_choice += timedelta(minutes=30)

        context = {
            "this_user": this_user,
            "employees": User.objects.all(),
            "today_quote": today_quote,
            "this_user_points": round(this_user.total_points, 2),
            "all_users_points": all_users_points,
            "clocks": clocks,
            "last_clock": last_clock,
            "date_cur": datetime.now().strftime("%H:%M %p. | %d-%M-%Y "),
            "last_clockout_choices": last_clockout_choices
        }
        return render(request, 'admin.html', context)
    elif this_user.user_level < 9:
        return redirect('/clockinout')
    else:
        return redirect('/')


def edit_quote(request, id):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id and this_user.user_level == 9:
        this_quote = Quote.objects.get(id=id)
        this_quote.onEdit = True
        this_quote.save()
        return redirect('/admin')
    elif this_user.user_level < 9:
        return redirect('/clockinout')
    else:
        return redirect('/')


def update_quote(request, id):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id and this_user.user_level == 9:
        this_quote = Quote.objects.get(id=id)
        this_quote.quote = request.POST['quote']
        this_quote.author = request.POST['author']
        this_quote.onEdit = False
        this_quote.save()
        return redirect('/admin')
    elif this_user.user_level < 9:
        return redirect('/clockinout')
    else:
        return redirect('/')


def award_extra_verify(request, id):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id=this_id)
    if this_id:
        award_user = User.objects.get(id=id)
        award_points = float(request.POST['point_value'])
        print(award_points)
        new_award = Award.objects.create(
            admin=this_user, user=award_user, points=award_points)
        return redirect('/admin')
    else:
        return redirect('/')
