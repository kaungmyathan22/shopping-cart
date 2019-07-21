from django.urls import path
from .views import product_list, product_detail

app_name = "product"

urlpatterns = [
    path('', product_list, name="list"),
    path('detail/<slug:slug>/', product_detail, name="detail"),
    path('category/<slug:slug>/', product_list, name="category"),
]
