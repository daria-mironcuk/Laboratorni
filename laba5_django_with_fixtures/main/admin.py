from django.contrib import admin
from .models import Brand, Sneaker

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'founded_year', 'is_active')
    search_fields = ('name', 'country')

@admin.register(Sneaker)
class SneakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'size', 'color', 'price', 'in_stock', 'created_at')
    list_filter = ('brand', 'color', 'size', 'in_stock')
    search_fields = ('name', 'brand__name')
