from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def login_verify(request):
    found_user = User.objects.filter(email=request.POST['email_address'])
    if len(found_user) < 1:
        messages.error(request, 'Invalid Credentials')
        return redirect('/')
    else:
        logged_user = found_user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['this_user_id'] = logged_user.id
            return redirect('/dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('/')

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    elif request.POST['password_confirm'] != request.POST['password']:
        messages.error(request, 'The password entered twice must be the same!')
    else:
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        user_pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        this_user = User.objects.create(email=email, first_name=first_name, last_name=last_name, password=user_pwd)
        request.session['this_user_id'] = this_user.id
        first_user = User.objects.first()
        first_user.user_level = 9
        messages.success(request, "Register successfully!")
        return redirect('/dashboard')