from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):

    list_display = ('order', 'product', 'quantity', 'price', )

    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''Admin View for Order'''

    list_display = ('first_name', 'last_name', 'email',
                    'phone', 'city', 'address', 'paid', )
    list_filter = ('city', 'paid')
    inlines = [
        OrderItemInline,
    ]
