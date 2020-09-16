from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.actor)
admin.site.register(models.movieSlice)
admin.site.register(models.comment)
admin.site.register(models.connect)