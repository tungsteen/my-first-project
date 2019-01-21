import unittest

from scripts.lesson1 import add


class MyFirstTest(unittest.TestCase):
    def test__add(self):
        result = add(8, 12)
        self.assertEqual(20, result)
