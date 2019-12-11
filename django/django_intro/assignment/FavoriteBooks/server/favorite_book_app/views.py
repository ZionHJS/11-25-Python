from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def regisration(request):
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
        this_user = User.objects.create(first_name=first_name, last_name=last_name, email=email, password=user_pwd)
        request.session['this_user_id'] = this_user.id
        messages.success(request, "Register successfully!")
        return redirect('/books')

def login(request):
    found_user = User.objects.filter(email=request.POST['email'])
    if len(found_user) < 1:
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    else:
        logged_user = found_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['this_user_id'] = logged_user.id
            return redirect('/books')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')

def books(request):
    this_id = request.session.get('this_user_id')
    if this_id is None:
        return redirect('/')
    else:
        this_user = User.objects.get(id = this_id)
        context={
            "this_user":this_user,
            "books":Book.objects.all()
        }
        return render(request, 'books.html', context)

def add_book(request):
    this_id = request.session.get('this_user_id')
    book_title = request.POST['book_title']
    book_des = request.POST['book_des']
    Book.objects.create(title=book_title, description=book_des, user=User.objects.get(id=this_id))
    return redirect('/books')

def logout(request):
    request.session.clear()
    return redirect('/')

def show_book(request, id):
    this_id = request.session.get('this_user_id')
    this_book = Book.objects.get(id=id)
    context = {
        'this_book':this_book
    }
    return render(request, 'show_book.html', context)

def update_book(request, id):
    this_id = request.session.get('this_user_id')
    update_book = Book.objects.get(id=id)
    book_title = request.POST['book_title']
    book_des = reqeust.POST['book_des']
