from django.conf.urls import include, url, patterns
from . import views

urlpatterns = patterns('',
    url(r'^register/$', 'accounts.views.register'),
    url(r'^login/$', 'accounts.views.login'),
    url(r'^profile/$', 'accounts.views.profile'),
    url(r'^logout/$', 'accounts.views.logout'),
     url(r'^$', 'accounts.views.index' ),
)
