from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import News, Comment

"""
# Create your views here.
def index(request):
    temp_name = 'homepage/index.html'
    return render(request=request, template_name=temp_name)
"""

class NewsList(ListView):
    model = News
    template_name = 'homepage/index.html'

class NewsDetail(DetailView):
    model = News
    template_name = 'homepage/detail_news.html'