from django.urls import path
from .views import cart_add, cart_detail, cart_remove

app_name = "cart"

urlpatterns = [
    path('add/<slug:product_slug>', cart_add, name="add"),
    path('detail/', cart_detail, name="detail"),
    path('remove/<slug:slug>/', cart_remove, name="remove"),
]
