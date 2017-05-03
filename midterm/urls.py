"""midterm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from midterm.views import loginview,auth_and_login,sign_up_in,secured,logout_view,regsec


urlpatterns = (
   url(r'^logout/$', logout_view),
   url(r'^login/$', loginview),
   url(r'^regsec/$', regsec),

   url(r'^auth/$', auth_and_login),
   url(r'^signup/$', sign_up_in),
   url(r'^secured/$', secured),
)