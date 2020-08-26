import unittest

from printcomic.collator import order_in_japan_style, order_in_western_style


class TestCollator(unittest.TestCase):
    def test_western(self):
        self.assertEqual(
            order_in_western_style(10), [12, 1, 2, 11, 10, 3, 4, 9, 8, 5, 6, 7]
        )

    def test_japan(self):
        self.assertEqual(
            order_in_japan_style(10), [7, 6, 5, 8, 9, 4, 3, 10, 11, 2, 1, 12]
        )


if __name__ == "__main__":
    unittest.main()
