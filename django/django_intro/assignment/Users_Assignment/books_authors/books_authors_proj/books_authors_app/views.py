from django.shortcuts import render
from .models import Book, Author

# Create your views here.
def index(request):
    context={
        'Books':Book.objects.all(),
        'Authors':Author.objects.all()
    }
    return render(request, 'index.html', context)

def show_book(request):
    
    context={
        
    }