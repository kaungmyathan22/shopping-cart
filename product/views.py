from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger
)

from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddForm
# Create your views here.


def product_list(request, slug=None):

    context = {}

    if slug:

        object_list = Product.objects.filter(category__slug=slug)
    else:

        object_list = Product.objects.all()

    paginator = Paginator(object_list, 9)

    page = request.GET.get('page')

    try:

        products = paginator.page(page)

    except PageNotAnInteger:

        products = paginator.page(1)

    except EmptyPage:

        products = paginator.page(paginator.num_pages)

    context = {
        'products': products,
        'paginator': paginator,
        'slug': slug
    }

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
