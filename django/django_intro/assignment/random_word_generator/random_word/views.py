from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def generate(request):
    count = 0
    request.session['num'] = count+1
    