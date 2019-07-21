from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from product.models import Product
from django.views.decorators.http import require_POST
from .forms import CartAddForm
# Create your views here.


@require_POST
def cart_add(request, product_slug):

    form = CartAddForm(request.POST)

    cart = Cart(request)

    product = get_object_or_404(Product, slug=product_slug)

    if form.is_valid():

        print("form valid")

        cd = form.cleaned_data

        quantity = cd['quantity']

        cart.add(product, quantity=quantity)

    else:

        print("form not valid")

    # product = get_object_or_404(Product. slug=product_slug)

    # cart.add(product)

    return redirect('cart:detail')


def cart_remove(request, slug):

    cart = Cart(request)

    product = get_object_or_404(Product, slug=slug)

    cart.remove(product)

    return redirect("cart:detail")


def cart_detail(request):

    context = {
        'cart': Cart(request),
    }

    # return render(request, 'cart/detail.html')
    return render(request, 'cart/detail.html', context)
