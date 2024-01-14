from django.shortcuts import render

finches = [
    { 'name': 'Tweety Bird', 'breed': 'Canary', 'color': 'Yellow' },
    { 'name': 'Big Red', 'breed': 'Cardinal', 'color': 'Red' },
    { 'name': 'Newspaper', 'breed': 'Zebra Finch', 'color': 'Black and White' },
]
# Create your views here.
# Render home view - '/'
def home(request):
    return render(request, 'home.html')

# Render about page - '/about/'
def about(request):
    return render(request, 'about.html')

# Render finch index page - '/finches/'
def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })
