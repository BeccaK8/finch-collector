from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

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
    
    # Change the Default Sort
    class Meta: 
        ordering = ['name']


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    # Create a finch_id FK
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date} for {self.finch}"
    
    # Change the Default Sort
    class Meta: 
        ordering = ['-date']