from django.shortcuts import render
from .models import Finch

# Create your views here.
# Render home view - '/'
def home(request):
    return render(request, 'home.html')

# Render about page - '/about/'
def about(request):
    return render(request, 'about.html')

# Render finch index page - '/finches/'
def finches_index(request):
    finches = Finch.objects.all().order_by('name')
    return render(request, 'finches/index.html', {
        'finches': finches
    })
