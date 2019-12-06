from django.shortcuts import render, redirect
from .models import Book, Author

# Create your views here.
def index_book(request):
    context={
        'Books': Book.objects.all(),
        'Authors': Author.objects.all(),
    }
    return render(request, 'index_book.html', context)

def add_book(reqeust):
    book_title = reqeust.POST['title']
    book_des = reqeust.POST['book_des']
    Book.objects.create(title=book_title, desc_TEXT=book_des)
    return redirect('/')

def show_book(request, id):
    this_book = Book.objects.get(id=id)
    context={
        'book_title': Book.objects.get(id=id).title,
        'book_id': id,
        'book_des': Book.objects.get(id=id).desc_TEXT,
        'book_authors': this_book.publishers.all(),
        'Authors': Author.objects.all(),
    }
    return render(request, 'books_view.html', context)

def add_author2book(request, id):
    #print(request.POST)
    select_tag = request.POST['author_select']
    author2add = Author.objects.get(id = int(select_tag))
    this_book = Book.objects.get(id=id)
    this_book.publishers.add(author2add)
    return redirect(f'/books/{id}')

#author part
def index_author(request):
    context={
        'Books': Book.objects.all(),
        'Authors': Author.objects.all(),
    }
    return render(request, 'index_author.html', context)

def add_author(reqeust):
    author_first_name = reqeust.POST['first_name']
    author_last_name = reqeust.POST['last_name']
    author_notes = reqeust.POST['notes']
    Author.objects.create(first_name=author_first_name, last_name=author_last_name)
    return redirect('/authors')

def show_author(request, id):
    this_author = Author.objects.get(id=id)
    context={
        'author_first_name': Author.objects.get(id=id).first_name,
        'author_last_name':Author.objects.get(id=id).last_name,
        'author_id': id,
        'author_notes': Author.objects.get(id=id).notes,
        'author_books': this_author.books.all(),
        'Books': Book.objects.all(),
    }
    return render(request, 'author_view.html', context)

def add_book2author(request, id):
    #print(request.POST)
    select_tag = request.POST['book_select']
    book2add = Book.objects.get(id = int(select_tag))
    this_author = Author.objects.get(id=id)
    this_author.books.add(book2add)
    return redirect(f'/authors/{id}')