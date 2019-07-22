from django.test import TestCase, Client
from django.urls import reverse, resolve
from model_mommy import mommy
from order.views import checkout, order_create, download_pdf


class TestCheckoutPage(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("order:checkout")

        self.response = self.client.get(self.url)

    def test_page_status_with_empty_cart(self):

        self.assertEqual(self.response.status_code, 302)

    def test_page_status_with_cart(self):

        product = mommy.make("Product")

        url = reverse('cart:add', kwargs={
                      'product_slug': product.slug})

        response = self.client.post(url, data={
            'quantity': 3,
        })

        self.assertEqual(self.response.status_code, 302)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func, checkout)


class TestOrderCreate(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("order:create")

        self.response = self.client.post(self.url)

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

        response = self.client.post(self.url, data={
            'first_name': "kaung",
            'last_name': "kaung",
            'email': 'arkarhtethan@gmail.com',
            'phone': '09-444054610',
            'city': 'mdy',
            'address': 'somme address'
        })

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'order/thankyou.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func, order_create)


class TestPdfDownloadPage(TestCase):

    def setUp(self):

        self.client = Client()

        order = mommy.make("Order")

        self.url = reverse("order:download-pdf", kwargs={'order_id': order.id})

        self.response = self.client.post(self.url)

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func, download_pdf)

    def test_page_status(self):

        self.assertEqual(self.response.status_code, 200)
