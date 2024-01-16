from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
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

# Render finch detail page - '/finches/:id'
def finches_detail(request, finch_id):
    #find one finch using its id
    finch = Finch.objects.get(id=finch_id)
    return render(request, 'finches/detail.html', { 'finch': finch })

# Create View - inheriting from CBV CreateView
# Create new finches
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

# Update View - inheriting from CBV Update View
# Update existing finch
class FinchUpdate(UpdateView):
    model = Finch
    # cannot rename a Finch
    fields = [ 'breed', 'description', 'color', 'size_inches' ]
