from django.conf.urls import url,patterns,include
from django.views.generic import ListView , DetailView
from startup.models import startups
#from .import views

urlpatterns = [ url(r'^$','startup.views.create'),
                url(r'^intern/$',ListView.as_view(queryset=startups.objects.all(),
                                         template_name="startup/intern_list.html")),
               url(r'^intern/(?P<pk>\d+)$',DetailView.as_view(model=startups,
                                                       template_name = 'startup/intern_details.html'))
]


