from django.views import generic
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from startup.forms import startupForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

def create(request):
    if request.POST :
        form = startupForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/login/auth')
    else:
        form = startupForm()

    args= {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_startup.html',args)

