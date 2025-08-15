from django.contrib import admin
from .models import Product, ProductQRLink

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name','sku','price','currency','bitrix_id','is_active','created_at', 'photo')
    search_fields = ('name','sku')
    list_filter = ('is_active','currency')

@admin.register(ProductQRLink)
class ProductQRLinkAdmin(admin.ModelAdmin):
    list_display = ('id','product','token','is_active','created_at')
    list_filter = ('is_active',)
    search_fields = ('token','product__name')
