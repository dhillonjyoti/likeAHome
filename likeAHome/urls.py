"""likeAHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from front_app import views
from admin_app import views as backend

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('admin_app.urls')),
    url(r'^sign_in/$', views.sign_in),
    url(r'^$', views.front_index),
    url(r'^sign_up/$', backend.sign_up),
    url(r'^verify/$',views.verify),
    url(r'^log_in/$',views.log_in),
]
