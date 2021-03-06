from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from accounts.forms import UserRegistrationForm, UserLoginForm

def index(request):
    return render(request,'base.html')

def register(request, register_form=UserRegistrationForm):
    if request.method == "POST":
        form = register_form(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/accounts/')

            #user = auth.authenticate(email=request.POST.get('email'),
             #                        password=request.POST.get('password1'))

            #if user:
               # form.save()
               # messages.success(request, "You have successfully registered")
           
               # return redirect(reverse('profile'))

            #else:
               # messages.error(request, "unable to log you in at this time!")

    else:
        form = register_form()

    args = {'form':form}
    args.update(csrf(request))

    return render(request, 'register.html', args)



def login(request, success_url=None):
    
    if request.method == "POST":
        
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'),
                                    password=request.POST.get('password'))

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                if success_url:
                    return redirect(reverse(success_url))
                else:
                    return redirect(reverse('profile'))
            else:
                form.add_error(None, "Your email or password was not recognised")

    else:
        form = UserLoginForm()

    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'login.html', args)

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'profile.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))
