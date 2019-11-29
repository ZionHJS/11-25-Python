from flask import Flask, session, redirect, request, render_template
import random
import datetime

app = Flask(__name__)
app.secret_key = 'ThisIsASecret'  #by default falsk stores session into the cookie not safe so set the secret_key

#generate random number
def randomNum(start, end):   #public method
    num = random.randrange(start, end)
    return num

#judge earnOrAdd return true or false
def earnOrAdd():   #public method
    chance = randomNum(0, 2)
    if chance == 1:
        return True
    else:
        return False

def addActivity(num, action, location):   #public method
    timestamp = datetime.datetime.now()   #get the current time data
    if location == 'casino':
        if action == 'earned':
            earned = 'Earned %d from the casino! %s' % (num, timestamp)
            session['activity'].append(['earn', earned])
        elif action == 'lost':
            lost = 'Entered a casino and lost %d gold... Ouch %s' % (num, timestamp)
            session['activity'].append(['lost', lost])
        else:
            print ("error")
    elif location == 'farm':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    elif location == 'cave':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    elif location == 'house':
        session['activity'].append(['earn', 'Earned %d from the %s! %s' % (num, location, timestamp)])
    else:
        print ("error")

@app.route('/')
def index():
    if session['total'] == None:   # set the default value of total
        session['total'] = 0
    if session['activity'] == None:   # set the default value of activity
        session['activity'] = []
    return render_template('index.html', total=session['total'], activities=session['activity'])

# route to /process_money
@app.route('/process_money', methods=['POST'])
def calculateMoney():
    hiddenInput = request.form['hidden']
    if hiddenInput == 'farm':
        farmNum = randomNum(10, 21)
        session['total'] += farmNum
        addActivity(farmNum, 'earned', 'farm')
    elif hiddenInput == 'cave':
        caveNum = randomNum(5, 10)
        session['total'] += caveNum
        addActivity(caveNum, 'earned', 'cave')
    elif hiddenInput == 'house':
        houseNum = randomNum(2, 5)
        session['total'] += houseNum
        addActivity(houseNum, 'earned', 'house')
    elif hiddenInput == 'casino':
        casinoNum = randomNum(0, 50)
        chance = earnOrAdd()
        if chance == True:
            session['total'] += casinoNum
            addActivity(casinoNum, 'earned', 'casino')
        elif chance == False:
            session['total'] -= casinoNum
            addActivity(casinoNum, 'lost', 'casino')
        else:
            print ("Error")
    else:
        print ("Error")
    return redirect('/')  #redirect

@app.route('/clear', methods=['POST'])
def clear():
    session['total'] = 0
    session['activity'] = []
    return redirect('/')  #redirect

app.run(debug=True)