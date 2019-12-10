from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def regisration(request):
    return redirect('success')

def success(request):
    return render(request, 'success.html')