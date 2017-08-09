"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('software.urls')),
    url(r'^login/auth/', include('user.urls')),
    url(r'^profile/', include('Profile.urls')),
    url(r'^startup/', include('startup.urls')),
    url(r'^blog/', include('blog.urls')),
    #url(r'^startup/intern/', include('internship.urls')),
    url(r'^info/', include('interview.urls')),
    #url(r'^login/', include('login.urls')),
    url(r'^accounts/', include('accounts.urls')),
    
    
     

    

]