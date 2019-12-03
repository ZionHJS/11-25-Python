from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_user(request):
    print('Got Post Info......')
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    return render(request, 'index.html')
