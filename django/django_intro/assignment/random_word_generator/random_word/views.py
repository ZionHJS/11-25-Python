from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return render(request, 'index.html')

def generate(request):
    request.session['count'] += 1
    request.session['random_str'] = get_random_string(length=14)
    return redirect('/')

