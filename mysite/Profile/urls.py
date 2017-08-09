from django.conf.urls import url,patterns,include
from django.views.generic import ListView , DetailView
from Profile.models import entries
#from .import views

urlpatterns = [ url(r'^$','Profile.views.create'),
                url(r'^view/$',ListView.as_view(queryset=entries.objects.all(),
                                         template_name="Profile/list.html")),
               url(r'^view/(?P<pk>\d+)$',DetailView.as_view(model=entries,
                                                       template_name = 'Profile/details.html'))
]


