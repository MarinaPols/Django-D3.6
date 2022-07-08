#from django.shortcuts import render
#D3
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import Post

class NewsList(ListView):
    model = Post
    title_news = 'name'
    ordering = 'dateCreation'

    template_name = 'news.html'

    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_news'] = None
        return context

class NewsDetail(DetailView):
    model = Post

    template_name = 'new.html'

    context_object_name = 'new'

# Create your views here.
