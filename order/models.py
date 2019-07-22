from django.db import models
from product.models import Product


class Order(models.Model):

    first_name = models.CharField(max_length=120)

    last_name = models.CharField(max_length=120)

    email = models.EmailField()

    phone = models.CharField(max_length=12)

    city = models.CharField(max_length=120)

    address = models.CharField(max_length=120)

    paid = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def get_total_cost(self):

        return sum(item.get_cost() for item in self.items.all())

    def __str__(self):

        return f'Order {self.id}'


class OrderItem(models.Model):

    order = models.ForeignKey(
        to="Order", related_name="items", on_delete=models.CASCADE)

    product = models.ForeignKey(to=Product, on_delete=models.DO_NOTHING)

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(max_digits=15, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def get_cost(self):

        return self.price * self.quantity

    def __str__(self):

        return str(self.pk)
