from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category')
    prepopulated_fields = {'slug': ('product_name',)}


class VariationtAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active')


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationtAdmin)
