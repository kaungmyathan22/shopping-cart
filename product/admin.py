from django.contrib import admin
from .models import Product, Category
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('title', 'created', 'updated', 'slug', )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('title', 'category', 'price',
                    'created', 'updated', 'slug', )

    list_editable = ('category', 'price',)

    search_fields = ('title', 'category', 'price', 'slug', )

    list_filter = ['category', 'created']
