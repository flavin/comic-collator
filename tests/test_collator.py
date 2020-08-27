import unittest

from comic_collator.collator import (
    CollatedOrder,
    order_in_japan_style,
    order_in_western_style,
)


class TestCollator(unittest.TestCase):
    def test_western(self):
        self.assertEqual(
            order_in_western_style(10),
            CollatedOrder(front=[12, 1, 10, 3, 8, 5], back=[2, 11, 4, 9, 6, 7]),
        )

    def test_japan(self):
        self.assertEqual(
            order_in_japan_style(10),
            CollatedOrder(front=[5, 8, 3, 10, 1, 12], back=[7, 6, 9, 4, 11, 2]),
        )


if __name__ == "__main__":
    unittest.main()
