from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'dashboard/template.html')

def HomePageView(request, *args, **kwargs):
    return render(request, 'home.html', context={})