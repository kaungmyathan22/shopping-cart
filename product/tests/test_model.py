from django.test import TestCase, Client
from django.urls import reverse, resolve
from model_mommy import mommy
from product.models import Product, Category, image_upload_path
from utils.unique_slug_field_generator import unique_slug_generator


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

    def test_upload_field_with_model_instance(self):

        file_name = "hello.png"

        uploaded_file_name = image_upload_path(self.model_instance, file_name)

        expected = f'hello-{self.model_instance.slug}.png'

        self.assertEqual(uploaded_file_name, expected)

    def test_upload_field_without_model_instance(self):

        category = mommy.make("Category")

        model = Product(category, 'title', 12.99, 'test')

        file_name = "hello.png"

        uploaded_file_name = image_upload_path(model, file_name)

        self.assertNotEqual(uploaded_file_name, file_name)

    def test_slug_unique(self):

        category = mommy.make("Category")

        model = mommy.make("Product")
        # model = Product(category, 'title', 12.99, 'test')

        slug = unique_slug_generator(model)

        slug_2 = unique_slug_generator(model)

        self.assertNotEqual(slug, slug_2)


class TestCategorytModel(TestCase):

    def setUp(self):

        self.model_instance = mommy.make("Category")

    def test_instance(self):

        self.assertTrue(isinstance(self.model_instance, Category))

    def test_str(self):

        self.assertEqual(str(self.model_instance), self.model_instance.title)

    def test_slug(self):

        self.assertTrue(len(self.model_instance.slug) > 0)
