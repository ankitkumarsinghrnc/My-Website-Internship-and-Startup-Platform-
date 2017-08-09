from django.conf.urls import url, include
from django.views.generic import ListView , DetailView
from interview.models import Post

urlpatterns = [url(r'^$',ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],
                                         template_name="interview/interview.html")),
               url(r'^(?P<pk>\d+)$',DetailView.as_view(model=Post,
                                                       template_name = 'interview/Post.html'))]

