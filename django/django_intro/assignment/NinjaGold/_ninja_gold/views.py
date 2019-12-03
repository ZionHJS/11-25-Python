from django.shortcuts import render, redirect
import random
import datetime

def randomNum(start, end):
    num = random.randrange(start, end)
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

def process_farm(request):
    farmNum = randomNum(10,20)
    request.session['total_gold'] += farmNum
    return redirect('/')

def process_cave(request):
    caveNum = randomNum(5,10)
    request.session['total_gold'] += caveNum
    return redirect('/')

def process_house(request):
    houseNum = randomNum(2,5)
    request.session['total_gold'] += houseNum
    return redirect('/')

def process_casino(request):
    casinoNum = randomNum(0,50)
    chance = earnOrAdd()
    if chance == True:
        request.session['total_gold'] += casinoNum
    else:
        request.session['total_gold'] -= casinoNum
    return redirect('/')

