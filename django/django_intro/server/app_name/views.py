from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("this is the equivalent of @app.rout('/')!")
    #return render(request, 'index.html')

#couple of other method
def new(request):
    pass
def create(request):
    return redirect('/')
def show(request, number):
    return HttpResponse('placeholder to edit blog{number} with method named "edit"')
def edit(request, number):
    return HttpResponse('placeholder to edit blog{number}')
def destroy(request):
    pass
