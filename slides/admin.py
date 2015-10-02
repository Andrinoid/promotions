from django.contrib import admin
from slides.models import *

admin.site.register(Promotion)

class SlideAdmin(admin.ModelAdmin):
    list_display = ('id','headline','matrix','is_active','index')
    #search_fields = ('stock', 'color', 'image', 'is_active', 'bead_type', 'color_theme')
    #list_filter = ('bead_type',)
admin.site.register(Slide, SlideAdmin)