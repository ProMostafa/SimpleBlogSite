from django.shortcuts import render
from django.views.generic import ListView ,DetailView
from django.views.generic.edit import CreateView ,UpdateView ,DeleteView
from django.urls import reverse_lazy
# Create your views here.

from .models import Article

class ArticleListView(ListView):
	model=Article
	template_name='articles/home.html'
	context_object_name= 'objs'


class ArticleCreateView(CreateView):
	model=Article
	template_name='articles/article.html'
	fields= '__all__'


# While this view is executing, self.object will contain the object that the view is operating
class ArticleDetailView(DetailView):
	model=Article
	template_name='articles/details.html'
	context_object_name= 'obj'  



class ArticleUpdateView(UpdateView):
	model=Article
	template_name='articles/edit.html'
	fields=['title','text']


class ArticleDeleteView(DeleteView):
	model=Article
	template_name='articles/delete.html'
	context_object_name='obj' 
	success_url=reverse_lazy('home')