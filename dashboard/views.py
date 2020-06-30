from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dashboard/template.html')

def HomePageView(request, *args, **kwargs):
    return render(request, 'home.html', context={})

def dashboardPageView(request):
    return render(request, 'dashboard/examples/dashboard.html', context={})

def basePageView(request):
    return render(request, 'dashboard/layouts/base.html', context = {})

def userPageView(request):
    return render(request, 'dashboard/user.html') 