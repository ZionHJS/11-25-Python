from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Book, Review
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

def logout(request):
    request.session.clear()
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

def add(request):
    this_id = request.session.get('this_user_id')
    this_user = User.objects.get(id = this_id)
    authors = []
    books = Book.objects.all()
    if len(books):
        for book in books:
            authors.push(book.author)
    book_title = request.POST['book_title']
    if request.POST['select_book_author']:
        book_author = request.POST['select_book_author']
    else:
        book_author = request.POST['book_author']
    new_book = Book.objects.create(title=book_title, author=book_author)
    review_des = request.POST['review_des']
    review_rating = request.POST['review_rating']
    print(review_rating)
    new_review = Review.Objects.create(description=review_des, rating=review_rating, user=this_user, book=new_book)
    context={
            "this_user":this_user,
            "books":books,
            "authors":authors
    }
    return render(request, 'add.html')