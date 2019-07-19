from django.test import TestCase, Client
from django.urls import reverse, resolve
from model_mommy import mommy
from product.models import Product, Category


class TestProductModel(TestCase):

    def setUp(self):

        self.model_instance = mommy.make("Product")

    def test_instance(self):

        self.assertTrue(isinstance(self.model_instance, Product))

    def test_str(self):

        self.assertEqual(str(self.model_instance), self.model_instance.title)

    def test_price(self):

        self.assertTrue(self.model_instance.price > 0)

    def test_slug(self):

        self.assertTrue(len(self.model_instance.slug) > 0)


class TestCategorytModel(TestCase):

    def setUp(self):

        self.model_instance = mommy.make("Category")

    def test_instance(self):

        self.assertTrue(isinstance(self.model_instance, Category))

    def test_str(self):

        self.assertEqual(str(self.model_instance), self.model_instance.title)

    def test_slug(self):

        self.assertTrue(len(self.model_instance.slug) > 0)
