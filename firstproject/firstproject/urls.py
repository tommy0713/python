"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.urls import re_path as url 
from userapp.views import * 


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^delSession/(\w+)/$',delSession),
    url(r'^readSession/(\w+)/$',readSession),
    url(r'^setSession/(\w+)/(\w+)/$',setSession),

    url(r'^delCookie/(\w+)/$',delCookie),
    url(r'^readCookie/(\w+)/$',readCookie),
    url(r'^setCookie/(\w+)/(\w+)/$',setCookie),
    url(r'^setCookieRed/(\w+)/(\w+)/$',setCookieRed),

    url(r'^$', index1),
    url(r'^index/$', index2),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    # url(r'^logincheck/$', logincheck),
    url(r'^useradd/$', useradd),
    url(r'^userlist/$', userlist),
    url(r'^userdelete/(\w+)/$', userdelete),
    url(r'^userdelete/$', userdelete),
    url(r'^userupdate/(\w+)/$', userupdate),
    url(r'^userupdate/$', userupdate),
    url(r'^userupdatecheck/$', userupdatecheck),
    url(r'^userinput/$', userinput),

]

