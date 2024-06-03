from django.contrib import admin
from .models import *
 
class GFGAdmin(admin.ModelAdmin):
    list_display = ['hotel_name', 'hotel_price', 
                    'hotel_description']
 
admin.site.register(GFG, GFGAdmin)
