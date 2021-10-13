from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from contacts.models import Contact

# Create your views here.

def register(request):
    if request.method == 'POST':
      #Get Value
      first_name = request.POST['first_name']
      last_name = request.POST['last_name']
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      confirm_password = request.POST['confirm_password ']

      #Check password validation
      if password == confirm_password:
          #Check username
          if User.objects.filter(username=username).exists():
              messages.error(request,'Username Already Exists')
              return redirect('register')
          else:
            if User.objects.filter(email=email).exists():
                messages.error(request,'Email Already Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password,
                first_name=first_name,last_name=last_name,email=email)
                #Login user
                #auth.login(request,user)
                #messages.success(request,'You are now logged in')
                #return redirect ('index')
                user.save()
                messages.success(request, 'Registration successful')
                return redirect('login')
      else:
         messages.error(request, 'Passwords does not match!')
         return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
       username = request.POST['username']
       password = request.POST['password']

       user = auth.authenticate(username=username, password=password)
       if user is not None:
           auth.login(request, user)
           messages.success(request, 'Logged in successfully')
           return redirect('dashboard')
       else:
            messages.error(request, 'Invalid Login Details')
            return redirect ('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)

    context = {
        'contacts': user_contacts,
    }
    return render(request, 'accounts/dashboard.html',context)
