"""notavampire URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from notavampire.views import *

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^polls/',include('polls.urls')),
    url(r'^nav/', NavFetch.as_view(), name='nav'),
    url(r'^loaddep/', DepFetch.as_view(), name='loaddep'),
    url(r'^about/', AboutFetch.as_view(), name='about'),
    url(r'^footer/', FooterFetch.as_view(), name='footer'),
    url(r'^contact/', ContactFetch.as_view(), name='contact'),    
]
handler404 = 'notavampire.views.page_not_found'
handler500 = 'notavampire.views.handler500'
