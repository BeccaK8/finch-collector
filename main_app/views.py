from django.shortcuts import render, redirect

# import Class-based Views (CBVs)
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch, Feeder
from .forms import FeedingForm

# Create your views here.
# Render home view - '/'
def home(request):
    return render(request, 'home.html')

# Render about page - '/about/'
def about(request):
    return render(request, 'about.html')

# Render finch index page - '/finches/'
def finches_index(request):
    finches = Finch.objects.all()
    return render(request, 'finches/index.html', {
        'finches': finches
    })

# Render finch detail page - '/finches/:id'
def finches_detail(request, finch_id):
    #find one finch using its id
    finch = Finch.objects.get(id=finch_id)

    #instantiate FeedingForm to be rendered in template
    feeding_form = FeedingForm()

    return render(request, 'finches/detail.html', { 'finch': finch, 'feeding_form': feeding_form })

# Save feeding and redirect
def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)
    # validate the form
    if form.is_valid():
        # don't save it to DB until the finch_id has been assigned
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


# Create View - inheriting from CBV CreateView
# Create new finches
class FinchCreate(CreateView):
    model = Finch
    fields = '__all__'

# Update View - inheriting from CBV UpdateView
# Update existing finch
class FinchUpdate(UpdateView):
    model = Finch
    # cannot rename a Finch
    fields = [ 'breed', 'description', 'color', 'size_inches' ]

# Delete View - inheriting from CBV DeleteView
# Delete existing finch
class FinchDelete(DeleteView):
    model = Finch
    success_url = '/finches'


### FEEDER views
    
# Feeder List
class FeederList(ListView):
    model = Feeder
    template_name = 'feeders/index.html'

# Feeder Detail
class FeederDetail(DetailView):
    model = Feeder
    template_name = 'feeders/detail.html'    

# Feeder Create
# Feeder Update
# Feeder Delete
    
