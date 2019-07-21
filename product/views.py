from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)

from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddForm
# Create your views here.


def product_list(request):

    context = {}

    object_list = Product.objects.all()

    if object_list:

        paginator = Paginator(object_list, 9)

        page = request.GET.get('page')

        try:

            products = paginator.page(page)

        except PageNotAnInteger:

            products = paginator.page(1)

        except EmptyPage:

            products = paginator.page(paginator.num_pages)

            # products = object_list

        context = {
            'products': products,
            'paginator': paginator,
        }

    else:

        context['products'] = object_list

    context['categories'] = Category.objects.all()

    return render(request, 'product/product_list.html', context)


def product_detail(request, slug):

    context = {}

    form = CartAddForm()

    product = get_object_or_404(Product, slug=slug)

    context.update({
        'product': product,
        'form': form,
    })

    return render(request, 'product/product_detail.html', context)
