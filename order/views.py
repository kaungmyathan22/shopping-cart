from django.shortcuts import render
from .forms import OrderCreateForm
# Create your views here.


def order_create(request):

    form = OrderCreateForm(request.POST or None)

    context = {
        'form': form
    }

    return render(request, 'order/order_create.html', context)
