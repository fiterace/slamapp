from django.urls import path
from dashboard import views

from .views import *

#template tagging
app_name = 'myapp'

urlpatterns = [

    path('', HomePageView, name='home'),
    path('dashboard', dashboardPageView, name="dashboard"),
    path('base', basePageView, name="base"),
    path('user', userPageView, name="user"),
    path('showSlambooks_all', showSlambooksAll.as_view(), name="showSlambooks_all"),
    path('showSlambooks_my', showSlambooksMyListView.as_view(), name="showSlambooks_my"),
    path('showentry/<int:pk>', showSlambookMyDetailView.as_view(), name="showentry"),
    path('fill_slambook_entry', fillSlambook_PageView, name='fill_slambook_entry'),
    path('letter', letterPageView, name="letter"),
]