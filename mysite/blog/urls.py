from django.conf.urls import url, include
from django.views.generic import ListView , DetailView
from blog.models import post

urlpatterns = [url(r'^$',ListView.as_view(queryset=post.objects.all().order_by("-date")[:25],
                                         template_name="blog/blog.html")),
               url(r'^(?P<pk>\d+)$',DetailView.as_view(model=post,
                                                       template_name = 'blog/post.html'))]
