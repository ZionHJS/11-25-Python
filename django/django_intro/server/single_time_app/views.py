from django.shortcuts import render
from time import gmtime, strftime

# Create your views here.
def showTime(request):
    context = {
        'time':strftime('%Y-%m-%d %H:%M %p', gmtime())
    }
    return render(request, 'single_time_app/index.html', context)
