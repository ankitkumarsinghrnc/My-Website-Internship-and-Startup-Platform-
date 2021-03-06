from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf



def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',c)
def auth_view(request):
    username = request.post.get('username','')
    password = request.post.get('password','')
    user = auth.authenticate(username=username , password=password)

    if user is not None:
        auth.login(request , user)
        return HttpresponseRedirect('/login/loggedin')
    else:
        return HttpresponseRedirect('/login/invalid')

def loggedin(request):
   return render_to_response('loggedin.html',
                              {'full_name':request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')

