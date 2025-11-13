from django.test import TestCase
from .models import Category, Product

class SimpleTest(TestCase):
    def test_create_category_and_product(self):
        c = Category.objects.create(name='Teste')
        p = Product.objects.create(name='X', description='x', price=9.99, category=c)
        self.assertEqual(p.category, c)
