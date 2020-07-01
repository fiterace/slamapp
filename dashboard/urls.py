from django.urls import path
from dashboard import views

from .views import HomePageView, dashboardPageView, basePageView, userPageView, showSlamBooks_all_PageView, show_slambook_entry_PageView

urlpatterns = [

    path('', HomePageView, name='home'),
    path('dashboard', dashboardPageView, name="dashboard"),
    path('base', basePageView, name="base"),
    path('user', userPageView, name="user"),
    path('showSlambooks_all',showSlamBooks_all_PageView, name="showSlambooks_all"),
    path('show_slambook_entry', show_slambook_entry_PageView, name="show_slambook_entry"),
    # naman's work
    # path('',views.index,name='index'),
    path('fillSlambook/',views.form_view,name='form_view')

]