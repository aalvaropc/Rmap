from django.contrib import admin
from .models import RecyclingLocation

@admin.register(RecyclingLocation)
class RecyclingLocationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address', 'latitude', 'longitude')
    list_display_links = ('name',)
    list_per_page = 10
