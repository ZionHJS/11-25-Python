from django.shortcuts import render
import random
import datetime

def randomNum(start, end):
    num = random.randrage(start, end)
    return num

def earnOrAdd():
    chance = randomNum(0,2)
    if change == 1:
        return True
    else:
        return False



# Create your views here.
def index(request):
    return render(request, 'index.html')

def process(request):
    