from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show

# Create your views here.
def index(request):
    return render(request, 'index.html')

def shows(request):
    all_shows = Show.objects.all()
    context = {
        'all_shows':all_shows
    }
    return render(request, 'shows.html', context)

def shows_new(request):
    return render(request, 'shows_new.html')

def create_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        new_title = request.POST['add_title']
        new_network = request.POST['add_network']
        new_date = request.POST['add_date']
        #print(new_date)
        new_des = request.POST['add_des']
        this_new_show = Show.objects.create(title=new_title, network=new_network, release_date=new_date, description=new_des)
        messages.success(request, 'Show successfully created!')
        print(messages)
    return redirect(f'/shows/{this_new_show.id}')

def show_this_show(request, id):
    this_show = Show.objects.get(id = id)
    #print(this_show)
    context = {
        'this_show':this_show
    }
    return render(request, 'shows_this_show.html', context)

def edit_show(request, id):
    this_show = Show.objects.get(id = id)
    context = {
        'this_show':this_show
    }
    return render(request, 'edit_show.html', context)

def edit_show_update(request, id):
    errors = Show.objects.basic_update_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        this_show = Show.objects.get(id = id)
        this_show.title = request.POST['update_title']
        this_show.network = request.POST['update_network']
        this_show.date = request.POST['update_date']
        this_show.description = request.POST['update_des']
    messages.success(request, 'Show successfully updated!')
    return redirect(f'/shows/{this_show.id}')

def delete_show(request, id):
    this_show = Show.objects.get(id = id)
    this_show.delete()
    return redirect('/shows')

