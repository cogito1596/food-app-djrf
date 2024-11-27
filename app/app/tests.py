from django.test import SimpleTestCase
from .calc import add


class TestSimple(SimpleTestCase):
    def test_add(self):
        self.assertEqual(add(3, 8), 11)
