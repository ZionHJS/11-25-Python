from django.shortcuts import render
# Create your views here.
def index(request):
    context = {
        #'all_the_users':User.objects.all()
    }
    return render(request, 'index.html')

