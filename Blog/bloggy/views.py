from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'page_name': 'Home Page',
    }
    return render(request, 'home.html', context)