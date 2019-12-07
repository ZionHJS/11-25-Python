from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')
    
def shows_new(request):
    #not done
    return render(request, 'shows_new.html')

def edit_tvshow(request):
    #not done
    return render(request, 'edit_show.html')

def delete_tvshow(request):
    #not done
    return redirect('/shows/new')