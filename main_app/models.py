from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=100, default=None)
    breed = models.CharField(max_length=100, default=None)
    description = models.TextField(max_length=250, default=None)
    color = models.CharField(max_length=100, default=None)
    size_inches = models.IntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'finch_id': self.id })
