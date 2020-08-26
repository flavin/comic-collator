import os
import unittest

from printcomic.image_writer import get_image_name


class TestCollator(unittest.TestCase):
    def test_get_image_name(self):
        path = os.path.dirname(os.path.abspath(__file__)) + "/fixtures/"
        self.assertEqual(
            get_image_name(path, 1, "jpg", "000.jpg"), "{}1.jpg".format(path)
        )
        self.assertEqual(
            get_image_name(path, 2, "jpg", "000.jpg"), "{}02.jpg".format(path)
        )
        self.assertEqual(
            get_image_name(path, 999, "jpg", None), "{}999.jpg".format(path)
        )

        self.assertEqual(get_image_name(path, 1, "png", "000.jpg"), "000.jpg")
        self.assertEqual(get_image_name(path, 3, "jpg", "000.jpg"), "000.jpg")
        self.assertRaises(FileNotFoundError, get_image_name, ".", 1, "jpg", None)
        self.assertRaisesRegex(
            FileNotFoundError, "File not found\(1\.jpg or 01\.jpg or 001\.jpg\)",
            get_image_name, ".", 1, "jpg", None )
        self.assertRaisesRegex(
            FileNotFoundError, "File not found\(11\.jpg or 011\.jpg\)",
            get_image_name, ".", 11, "jpg", None )
        self.assertRaisesRegex(
            FileNotFoundError, "File not found\(111\.jpg\)",
            get_image_name, ".", 111, "jpg", None )