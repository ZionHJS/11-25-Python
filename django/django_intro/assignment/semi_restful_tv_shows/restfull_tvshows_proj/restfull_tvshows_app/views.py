from django.shortcuts import render, redirect
from .models import Show

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create_show(request):
    new_title = request.POST['add_title']
    new_network = request.POST['add_network']
    new_date = request.POST['add_date']
    new_des = request.POST['add_des']
    context = {
        'new_title':newtitle,
        'new_network':new_network,
        'new_date':new_date,
        'new_des':new_des
    }
    return redirect('/shows/{{id}}', context)
    
def shows_new(request):
    #not done
    return render(request, 'shows_new.html')

def edit_tvshow(request):
    #not done
    return render(request, 'edit_show.html')

def delete_tvshow(request):
    #not done
    return redirect('/shows/new')