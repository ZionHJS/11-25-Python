from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
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

def signin_verify(request):
    found_user = User.objects.filter(email=request.POST['email_address'])
    if len(found_user) < 1:
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    else:
        logged_user = found_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['this_user_id'] = logged_user.id
            return redirect('/dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')

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
        first_user = User.objects.first()
        first_user.user_level = 9
        messages.success(request, "Register successfully!")
        return redirect('/dashboard')

def dashboard(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    users = User.objects.all()
    if this_user is not None:
        if this_user.user_level<9:
            context={
            "users":users,
            "admin_num":9
            }
            return render(request, 'user_dashboard.html', context)
        else:
            context={
            "users":users,
            "admin_num":9
            }
            return render(request, 'admin_dashboard.html', context)
    else:
        return redirect('/')

def add_new(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    if this_user is not None and this_user.user_level >= 9:
        return render(request, 'add_new.html')
    else:
        return redirect('/')

def add_new_verify(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    if this_user is not None and this_user.user_level >= 9:
        errors = User.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        elif request.POST['password_confirm'] != request.POST['password']:
            messages.error(request, 'The password entered twice must be the same!')
        else:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            password = request.POST['password']
            user_pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=user_pwd)
            messages.success(request, "Register successfully!")
            return redirect('/dashboard')
    else:
        return redirect('/users/new')

def admin_edit_user(request, id):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    edit_user = User.objects.get(id = id)
    if this_user is not None and this_user.user_level >= 9:
        context={
            "edit_user":edit_user
        }
        return render(request, 'admin_edit_user.html', context)
    else:
        return redirect('/dashboard')

def admin_remove_user(request, id):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    remove_user = User.objects.get(id = id)
    if this_user is not None and this_user.user_level >= 9:
        remove_user.delete()
        return redirect('/dashboard')
    else:
        return redirect('/dashboard')

def edit_self(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    if this_user is not None:
        context={
            "this_user":this_user
        }
        return render(request, 'edit_self.html', context)
    else:
        return redirect('/')

def show_user(request, id):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    show_user = User.objects.get(id = id)
    if this_user is not None:
        context={
            "this_user":this_user,
            "show_user":show_user,
            "messages_all":show_user.messages_own.all()
        }
        return render(request, 'show_user.html', context)
    else:
        return redirect('/')

def leave_message(request, id):
    errors = Message.objects.basic_validator_message(request.POST)
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/users/show/{id}')
    elif this_user is not None:
        show_user = User.objects.get(id = id)
        message_content = request.POST['message_content']
        new_message = Message.objects.create(content=message_content, msg_author=this_user, msg_owner=show_user)
        return redirect(f'/users/show/{id}')

def leave_comment(request, uid, mid):
    errors = Comment.objects.basic_validator_comment(request.POST)
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/users/show/{uid}')
    elif this_user is not None:
        show_user = User.objects.get(id = uid)
        this_message = Message.objects.get(id = mid)
        comment_content = request.POST['comment_content']
        new_comment = Comment.objects.create(content=comment_content, author=this_user, message=this_message)
        return redirect(f'/users/show/{uid}')

def update_info(request):
    errors = User.objects.basic_validator_info(request.POST)
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/edit')
    elif this_user is not None:
        this_user.email = request.POST['update_email']
        this_user.first_name = request.POST['update_first_name']
        this_user.last_name = request.POST['update_last_name']
        this_user.save()
        users = User.objects.all()
        context={
            "users":users,
            "admin_num":9
        }
        return render(request, 'user_dashboard.html', context)
    else:
        return redirect('/')

def update_password(request):
    errors = User.objects.basic_validator_password(request.POST)
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/edit')
    elif request.POST['update_password_confirm'] != request.POST['update_password']:
        messages.error(request, 'The password entered twice must be the same!')
    elif this_user is not None:
        this_user.password = request.POST['update_password']
        this_user.save()
        users = User.objects.all()
        context={
            "users":users,
            "admin_num":9
        }
        return render(request, 'user_dashboard.html', context)
    else:
        return redirect('/')

def update_des(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    if this_user is not None:
        this_user.des = request.POST['update_des']
        this_user.save()
        users = User.objects.all()
        context={
            "users":users,
            "admin_num":9
        }
        return render(request, 'user_dashboard.html', context)
    else:
        return redirect('/')

def admin_update_info(request, id):
    errors = User.objects.basic_validator_info(request.POST)
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    edit_user = User.objects.get(id = id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/edit')
    elif this_user is not None and this_user.user_level >= 9:
        edit_user.email = request.POST['update_email']
        edit_user.first_name = request.POST['update_first_name']
        edit_user.last_name = request.POST['update_last_name']
        if request.POST['admin_normal'] == "admin":
            edit_user.user_level = 9
        elif request.POST['admin_normal'] == "normal":
            edit_user.user_level = 1
        else:
            edit_user.user_level = 0
        edit_user.save()
        users = User.objects.all()
        context={
            "users":users,
            "admin_num":9
        }
        return redirect('/dashboard')
    else:
        return redirect('/')

def admin_update_password(request, id):
    errors = User.objects.basic_validator_password(request.POST)
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    edit_user = User.objects.get(id = id)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/users/edit')
    elif request.POST['update_password_confirm'] != request.POST['update_password']:
        messages.error(request, 'The password entered twice must be the same!')
    elif this_user is not None and this_user.user_level >= 9:
        edit_user.password = request.POST['update_password']
        edit_user.save()
        users = User.objects.all()
        context={
            "users":users,
            "admin_num":9
        }
        return redirect('/dashboard')
    else:
        return redirect('/')