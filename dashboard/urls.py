from django.contrib import admin
from django.conf.urls import url, include
from dashboard import views
from django.urls import path

# TEMPLATE TAGGING
app_name = 'dashboard'

urlpatterns = [
    url(r'^$',views.index,name='index'),
]