from django.shortcuts import render, HttpResponse, redirect
def empty(request):
    return HttpResponse('this is the empty')

# Create your views here.
def index(request, name):
    # return HttpResponse("this is the equivalent of @app.rout('/')!")
    context = {
        'name':name,
        'favorite_color':'turquoise',
        'pets':['Bruce', 'Fitz','Georgie']
    }
    return render(request, 'index.html', context)

#couple of other method
def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')
def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse(f'placeholder to edit blog {number} with method named "edit"')
def edit(request, number):
    return HttpResponse(f'placeholder to edit blog{number}')
def destroy(request):
    return redirect('/')
