from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'countInStock', 'is_published', 'list_date', 'photo_main')
    list_display_links = ('id', 'name')
    list_per_page = 10
    search_fields = ('id', 'name', 'price', 'countInStock', 'is_published', 'list_date')


admin.site.register(Item, ItemAdmin)
