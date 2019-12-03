from django.shortcuts import render
import random
import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def process(request):
    