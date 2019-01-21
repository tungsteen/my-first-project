import unittest

from scripts.lesson1 import add, sub


class MyFirstTest(unittest.TestCase):
    def test__add(self):
        result = add(8, 12)
        self.assertEqual(20, result)

    def test__sub(self):
        result = sub(12, 8)
        self.assertEqual(4, result)
