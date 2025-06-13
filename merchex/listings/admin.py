from django.contrib import admin
from .models import Band, Listing
# Register your models here.

class BandAdmin(admin.ModelAdmin):
    list_display = ('name', 'genre', 'year_formed', 'active',)
    search_fields = ('name', 'genre')
    list_filter = ('genre', 'year_formed', 'active')

class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'type', 'price', 'description', 'band')
    search_fields = ('title', 'description')
    list_filter = ('year', 'type')

admin.site.register(Band, BandAdmin)
admin.site.register(Listing, ListingAdmin)