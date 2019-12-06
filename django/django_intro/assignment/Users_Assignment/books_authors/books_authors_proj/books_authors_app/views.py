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

def show_book(request, id):
    context={
        'book_title':Book.object.get(id=id).title,
        'book_id':id,
        'book_des':Book.object.get(id=id).desc_TEXT,
        'book_author':Book.publishers.all(),
        'Authors':Author.objects.all(),
    }
    return render(request, 'books_view.html', context)

def add_author2book(request, id):
    