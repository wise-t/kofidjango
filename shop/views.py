from django.shortcuts import render
from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post #, Category,Comment
from .forms import PostForm
#from .forms import PostForm #, EditForm,CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.


class HomeView(ListView):
    model=Post.objects.all()
    template_name='index.html'

    def get_context_data(self,*args,**kwargs):
            cat_menu=AddItemView.objects.all()
            context=super(HomeView,self).get_context_data(*args,**kwargs)
            context["cat_menu"]=cat_menu
            return context



class AddItemView(CreateView): 
    model=Post
    form_class=PostForm
    template_name='new.html'
    # fields='__all__'

    def get_context_data(self,*args,**kwargs):
        cat_menu=Post.objects.all()
        context=super(AddItemView,self).get_context_data(*args,**kwargs)
        context["cat_menu"]=cat_menu
        return context
        
def index(request):

    Posts=Post.objects.all()
    
    return render (request,"index.html",{'Posts':Posts }) 