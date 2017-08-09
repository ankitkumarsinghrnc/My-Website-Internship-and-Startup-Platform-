from django.views import generic
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView,UpdateView, DeleteView
#from .models import entries
from Profile.forms import entriesForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf



#class IndexView(generic.ListView):
 #   template_name='profile/index.html'
  #  context_object_name = 'all_albums'

   # def get_queryset(self):
    #    return entries.objects.all()


#class DetailView(generic.DetailView):
 #   model = entries
  #  template_name = 'profile/detail.html'

#class entriesCreate(CreateView):
 #   models = entries
  #  fields = ['name','enrollment','date_of_birth','skills','more_about_you']


def create(request):
    if request.POST :
        form = entriesForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/login/auth')
    else:
        form = entriesForm()

    args= {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('create_entries.html',args)
