import uuid
import boto3
import os

from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# import Class-based Views (CBVs)
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Finch, Feeder, Photo
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

    # get the feeders not associated to the finch
    id_list = finch.feeders.all().values_list('id')
    feeders_finch_doesnt_have = Feeder.objects.exclude(id__in=id_list)

    #instantiate FeedingForm to be rendered in template
    feeding_form = FeedingForm()

    return render(request, 'finches/detail.html', { 
        'finch': finch, 
        'feeding_form': feeding_form,
        'feeders': feeders_finch_doesnt_have
    })

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

# Add Photo to cat
def add_photo(request, finch_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # handle any errors
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)

            # build the full url
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, finch_id=finch_id)
        except Exception as e:
            print('An error occurred uploading file to S3')
            print(e)
    return redirect('detail', finch_id=finch_id)

# Associate Feeder to Finch
def assoc_feeder(request, finch_id, feeder_id):
    Finch.objects.get(id=finch_id).feeders.add(feeder_id)
    return redirect('detail', finch_id=finch_id)

# Unassociate Feeder to Finch
def unassoc_feeder(request, finch_id, feeder_id):
    Finch.objects.get(id=finch_id).feeders.remove(feeder_id)
    return redirect('detail', finch_id=finch_id)


# Create View - inheriting from CBV CreateView
# Create new finches
class FinchCreate(CreateView):
    model = Finch
    fields = [ 'name', 'breed', 'description', 'color', 'size_inches' ]

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
class FeederCreate(CreateView):
    model = Feeder
    fields = [ 'name', 'location', 'food_type' ]

    def form_valid(self, form):
        return super().form_valid(form)
    
# Feeder Update
class FeederUpdate(UpdateView):
    model = Feeder
    fields = [ 'name', 'location', 'food_type' ]

# Feeder Delete
class FeederDelete(DeleteView):
    model = Feeder
    success_url = '/feeders'
