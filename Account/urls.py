from django.conf.urls import url,include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^Login/$', views.login),
    url(r'^Reg/$', views.register),
    url(r'^Reg/(?P<ReferenceId>(\d)*)/$', views.register),
    url(r'^ChangePwd/$', views.ChangePwd),
]
