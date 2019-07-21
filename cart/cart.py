from decimal import Decimal
from django.conf import settings
from product.models import Product
from .forms import CartAddForm


class Cart:

    def __init__(self, request=None):

        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:

            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

        # self.cart = {}

    def add(self, product, quantity=1, update=False):

        product_id = product.id

        if not product_id in self.cart:

            self.cart[product_id] = {
                'quantity': quantity,
            }

        elif update:

            self.cart[product_id]['quantity'] = quantity

        else:

            pass

        self.save()

        return None

    def save(self):

        self.session.modified = True

    def remove(self, product):

        product_id = str(product.id)

        if product_id in self.cart:

            del self.cart[product_id]

            self.save()

        else:

            raise ValueError("No such product in cart")

        return None

    def get_total_price(self):

        return sum(item.total_price for item in self)

    def __iter__(self):

        cart = self.cart.copy()

        items = []

        for i in cart:

            product = Product.objects.get(pk=i)

            product.quantity = cart[i]['quantity']

            product.total_price = Decimal(product.quantity) * product.price

            product.update_form = CartAddForm(
                initial={'quantity': product.quantity})

            items.append(product)

        for item in items:

            yield item

    def __len__(self):

        result = 0

        cart = self.cart.copy()

        for k in cart.values():

            result = result + int(k['quantity'])

        return result

    def __str__(self):

        return str(self.cart)
