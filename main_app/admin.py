from django.contrib import admin
from .models import Finch, Feeding, Feeder, Photo

# Register your models here.
admin.site.register(Finch)
admin.site.register(Feeding)
admin.site.register(Feeder)
admin.site.register(Photo)
