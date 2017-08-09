from django.conf.urls import url , include
from django.views.generic import ListView , DetailView
#from login.models import user
from . import views

urlpatterns = [#url(r'^$',ListView.as_view(queryset=user.objects.all()
                #                    ,template_name="login/login.html")),
               #url(r'^(?P<pk>\d+)$',DetailView.as_view(model=user,
                #                                       template_name = 'login/user.html')),


# user auth urls

   url(r'^$' , 'login.views.login'  ),
    url(r'^auth/$' , 'login.views.auth_view'  ),
    url(r'^logout/$' , 'login.views.logout' ),
    url(r'^loggedin/$' ,'login.views.loggedin' ),
    url(r'^invalid/$' , 'login.views.invalid_login'),

               ]
