from django.contrib import admin
from django.conf.urls import url, include
from dashboard import views
from django.urls import path

# TEMPLATE TAGGING
app_name = 'dashboard'

urlpatterns = [
    path('',views.index,name='index'),
    path('fillSlambook/',views.form_view,name='form_view')
]