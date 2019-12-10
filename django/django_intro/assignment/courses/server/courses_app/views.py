from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    courses = Course.objects.all()
    context = {
        'courses':courses
    }
    return render(request, 'index.html',context)

def add_course(request):
    course_name = request.POST['add_name']
    course_des = request.POST['add_des']
    Course.objects.create(course_name=course_name, description=course_des)
    context = {
        'courses':Course.objects.all()
    }
    return render(request, 'index.html', context)
    #return redirect('/')

def show_remove(request, id):
    remove_obj = Course.objects.get(id = id)
    context= {
        'this_course':remove_obj
    }
    return render(request, 'show_remove.html', context)

def remove(request, id):
    remove_obj = Course.objects.get(id = id)
    if request.POST['no']:
        return redirect('/')
    elif request.POST['yes']:
        remove_obj.remove()
        return redirect('/')