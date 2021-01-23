from django.urls import path,re_path
from.import views
from .views import AddItemView ,HomeView #, ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView,CategoryListView,LikeView,comment_approve,comment_remove
from . import views

#from django.contrib.auth import views


app_name='shop'
urlpatterns = [
    path('', views.index,name='index'),
    path('',HomeView.as_view(),name="index"),
    path('new/',AddItemView.as_view(),name='new'),

]
