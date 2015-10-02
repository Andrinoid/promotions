from snuddubond.models import *
from django.contrib import admin

class BeadAdmin(admin.ModelAdmin):
    list_display = ('stock', 'color', 'image', 'is_active', 'bead_type', 'material')
    search_fields = ('stock', 'color', 'image', 'is_active', 'bead_type', 'color_theme')
    list_filter = ('bead_type',)
admin.site.register(Bead, BeadAdmin)

admin.site.register(Preset)
#admin.site.register(User)
admin.site.register(Order)
admin.site.register(Stored_chain)

