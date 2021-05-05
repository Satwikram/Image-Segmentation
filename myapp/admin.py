from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Segmentation)
class SegmentModel(admin.ModelAdmin):

    list_filter = ('id', 'image', 'prediction')
    list_display = ('id', 'image', 'prediction')

