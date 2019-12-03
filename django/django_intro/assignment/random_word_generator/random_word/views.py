from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return render(request, 'index.html')

def generate(request):
    count = 0
    request.session['count'] = count+1
    random_str = get_random_string(length=14)
    