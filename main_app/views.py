from django.shortcuts import render

# Create your views here.
# Render home view - '/'
def home(request):
    return render(request, 'home.html')

# Render about page - '/about/'
def about(request):
    return render(request, 'about.html')
