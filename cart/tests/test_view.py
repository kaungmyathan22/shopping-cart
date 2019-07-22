from django.test import TestCase, Client
from django.urls import reverse, resolve
from model_mommy import mommy
from cart.views import cart_detail


class TestCartDetailPage(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("cart:detail")

        self.response = self.client.get(self.url)

    def test_page_status(self):

        self.assertEqual(self.response.status_code, 302)

    def test_order_create(self):

        product = mommy.make("Product")

        url = reverse('cart:add', kwargs={
                      'product_slug': product.slug})

        response = self.client.post(url, data={
            'quantity': 3,
        })

        self.assertEqual(self.response.status_code, 302)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'cart/detail.html')

    def test_cart_remove(self):

        product = mommy.make("Product")

        url = reverse('cart:add', kwargs={
                      'product_slug': product.slug})

        response = self.client.post(url, data={
            'quantity': 3,
        })

        self.assertEqual(self.response.status_code, 302)

        url = reverse('cart:remove', kwargs={'slug': product.slug})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_cart_form_invalid(self):

        product = mommy.make("Product")

        url = reverse('cart:add', kwargs={
                      'product_slug': product.slug})

        response = self.client.post(url, data={
            'quantity': 'hello',
        })

        self.assertEqual(self.response.status_code, 302)

    def test_cart_remove_with_empty_cart(self):
        product = mommy.make("Product")

        url = reverse('cart:remove', kwargs={'slug': product.slug})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func, cart_detail)
