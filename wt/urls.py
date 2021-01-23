"""wt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404,handler500
from django.conf import settings
from django.contrib.auth import views
from django.conf.urls.static import static

#from core import views as core_views

from .import views

handler404='wt.views.handler404'
handler500='wt.views.handler500'

urlpatterns = [
    
    path('', views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('destinations/',views.destinations,name='destinations'),
    path('elements/',views.elements,name='elements'),
    path('article1/',views.article1,name='article1'),
    path('settings/',views.settings,name='settings'),
    path('news/',views.news,name='news'),
    path('blog/', include('blog.urls')),
    path('members/',include('django.contrib.auth.urls')),
    path('members',include('members.urls')),
    path('shop',include('shop.urls')),


    #path('', core_views.HomeView.as_view(), name='home'),

    path('oauth/', include('social_django.urls', namespace='social')),
    
    path('admin/', admin.site.urls),

]

urlpatterns =urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns = [
#         path('__debug__/', include(debug_toolbar.urls)),
#     ] + urlpatterns