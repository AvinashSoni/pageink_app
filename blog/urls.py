from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = patterns('',
	                   url(r'^$', ListView.as_view(
	                   queryset=Post.objects.all().order_by("-date")[:10],
	                   template_name="blog.html")),

	                   url(r'^(?P<pk>\d+)$', DetailView.as_view(
	                   model = Post,
	                   template_name="post.html")),

	                   url(r'^archives/$', ListView.as_view(
	                   queryset=Post.objects.all().order_by("-date"),
	                   template_name="archives.html")),

	                   url(r'^latestnews/$', ListView.as_view(
	                   queryset=Post.objects.all().order_by("-date")[:5],
	                   template_name="latestnews.html")),

	                   url(r'^aboutus/$', ListView.as_view(
	                   queryset=Post.objects.all().order_by("-date")[:5],
	                   template_name="aboutus.html")),

	                   url(r'^carousel/$', ListView.as_view(
	                   queryset=Post.objects.all().order_by("-date")[:5],
	                   template_name="carousel.html")),


	                  )

# Create your views here.
