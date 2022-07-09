"""
Smaple tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    """
    test calc module
    """

    def test_add(self):
        res = calc.add(4, 5)
        self.assertEqual(res, 9)

    def test_substract(self):
        res = calc.subtract(20, 10)
        self.assertEqual(res, 10)
