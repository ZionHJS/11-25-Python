from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def shows_new(request):
    return render(request, 'shows_new.html')
