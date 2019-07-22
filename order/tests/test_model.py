from model_mommy import mommy
from django.test import TestCase
from order.models import Order, OrderItem


class TestOrderItemModel(TestCase):

    def setUp(self):

        self.model = mommy.make("OrderItem")

    def test_instance(self):

        self.assertTrue(isinstance(self.model, OrderItem))

    def test_str(self):

        self.assertEqual(str(self.model), str(self.model.id))

    def test_get_cost(self):

        expected = self.model.quantity * self.model.price

        self.assertEqual(self.model.get_cost(), expected)


class TestOrderModel(TestCase):

    def setUp(self):

        self.model = mommy.make("Order")

    def test_instance(self):

        self.assertTrue(isinstance(self.model, Order))

    def test_str(self):

        expected = f'Order {str(self.model.id)}'

        self.assertEqual(str(self.model), expected)

    def test_total_cost(self):

        expected = sum(item.quantity *
                       item.price for item in self.model.items.all())

        self.assertEqual(self.model.get_total_cost(), expected)
