from django.urls import path
from .views import order_create, checkout, thank_you, test, download_pdf

app_name = "order"

urlpatterns = [
    path('checkout/', checkout, name="checkout"),
    path('create/', order_create, name="create"),
    path('download/pdf/<int:order_id>/', download_pdf, name="download-pdf"),
]
