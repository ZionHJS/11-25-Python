from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index(request):
    context={
        'Books':Book.objects.all(),
        'Authors':Author.objects.all()
    }
    return render(request, 'index.html', context)

def add_book(reqeust):
    book_title = reqeust.POST['title']
    book_des = reqeust.POST['book_des']
    Book.objects.create(title=book_title, desc_TEXT=book_des)
    return redirect('/')

def show_book(request):
    context={
        
    }
    return render(request, 'books_view.html')