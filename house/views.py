from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from house.models import House
# Create your views here.

class Helloworld(TemplateView):
    template_name = 'test.html'

class PostsView(ListView):
    model = House
    template_name = 'index.html'

class PostDetailView(DetailView):
	    model = House
	    template_name = 'post_detail.html'