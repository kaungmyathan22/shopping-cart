from django.test import TestCase, Client
from django.urls import reverse, resolve
from model_mommy import mommy
from product.views import product_list, product_detail
from product.models import Product


class TestProductListPage(TestCase):

    def setUp(self):

        self.client = Client()

        self.url = reverse("product:list")

        self.response = self.client.get(self.url)

    def test_page_status(self):

        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):

        self.assertTemplateUsed(self.response, 'product/product_list.html')

    def test_page_not_an_integer(self):

        url = self.url+"?page="

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_page_empty(self):

        url = self.url+"?page=100"

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func, product_list)


class TestProductDetailPage(TestCase):

    def setUp(self):

        self.client = Client()

        self.model = mommy.make("Product")

        self.url = reverse("product:detail", kwargs={"slug": self.model.slug})

        self.response = self.client.get(self.url)

    def test_page_status(self):

        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):

        self.assertTemplateUsed(self.response, 'product/product_detail.html')

    def test_view_fun(self):

        view_fun = resolve(self.url)

        self.assertEqual(view_fun.func, product_detail)

    def test_404(self):

        url = reverse("product:detail", kwargs={'slug': 'hello'})

        res = self.client.get(url)

        self.assertEqual(res.status_code, 404)
