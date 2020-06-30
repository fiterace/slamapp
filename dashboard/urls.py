from django.urls import path

from .views import HomePageView, dashboardPageView, basePageView, userPageView

urlpatterns = [

    path('', HomePageView, name='home'),
    path('dashboard', dashboardPageView, name="dashboard"),
    path('base', basePageView, name="base"),
    path('user', userPageView, name="user"),
    # naman's work
    path('',views.index,name='index'),
    path('fillSlambook/',views.form_view,name='form_view')

]