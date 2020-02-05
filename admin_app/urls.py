from django.conf.urls import url
from admin_app import views


app_name = "admin_app"

urlpatterns = [
    url(r'^admin_register/$', views.admin_signup),
    url(r'^admin_index/$', views.admin_index),
    url(r'^pg_index/$', views.pg_index),
]