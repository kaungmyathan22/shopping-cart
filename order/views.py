import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import OrderCreateForm
from cart.cart import Cart
from django.views.decorators.http import require_POST
from order.models import OrderItem, Order
from django.template.loader import render_to_string
from django.conf import settings
from io import BytesIO
# Create your views here.


def thank_you(request):

    return render(request, 'order/thankyou.html')


@require_POST
def order_create(request):

    form = OrderCreateForm(request.POST or None)

    cart = Cart(request)

    if len(cart) <= 0:

        return redirect("product:list")

    if form.is_valid():

        order = form.save()

        for item in cart:

            OrderItem.objects.create(
                order=order,
                product=item,
                quantity=item.quantity,
                price=item.price
            )

        # order.save()

        cart.clear()

        context = {
            'order': order
        }

        return render(request, 'order/thankyou.html', context)


def checkout(request):

    cart = Cart(request)

    if len(cart) <= 0:

        return redirect("product:list")

    form = OrderCreateForm()

    context = {
        'form': form,
        'cart': cart
    }

    return render(request, 'order/order_create.html', context)


def test(request):

    context = {
        "order": Order.objects.last()
    }

    return render(request, 'order/pdf.html', context)


def download_pdf(request, order_id):

    order = get_object_or_404(Order, id=order_id)

    template = get_template('order/pdf.html')
    html = template.render({'order': order})
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
        return HttpResponse(response.getvalue(), content_type='application/pdf')
    else:
        return HttpResponse("Error Rendering PDF", status=400)
