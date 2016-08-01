from django.shortcuts import render
from django.views.generic import DetailView, ListView
from pinax.blog.models import Post
from django.http import HttpResponse



class ContactIzmirIndexView(ListView):
    model = Post
    template_name ="iletisim/iletisim_izmir.html"

class ContactManisaIndexView(ListView):
    model = Post
    template_name = "iletisim/iletisim_manisa.html"

class HomeIndexView(ListView):
    model = Post
    template_name = "home/index.html"
