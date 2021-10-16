import unittest
from models.rectangle import Rectangle


class TestRectangleMethod(unittest.TestCase):
    def test_00_case_width_success(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.width, 5)

    def test_01_case_height_success(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.height, 10)

    def test_02_case_x_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.x, 0)

    def test_03_case_y_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.y, 0)

    def test_04_case_id_default(self):
        new_obj = Rectangle(5, 10)
        self.assertEqual(new_obj.id, new_obj.id)

    def test_05_case_width_success_01(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.width, 8)

    def test_06_case_height_success_01(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.height, 12)

    def test_07_case_x_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.x, 5)

    def test_08_case_y_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.y, 3)

    def test_09_case_id_own(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertEqual(new_obj.id, 26)

    def test_10_case_instance_rectangle(self):
        new_obj = Rectangle(8, 12, 5, 3, 26)
        self.assertIsInstance(new_obj, Rectangle)

    def test_11_case_width_string(self):
        with self.assertRaises(TypeError):
            Rectangle("string", 12, 5, 3, 26)

    def test_12_case_height_string(self):
        with self.assertRaises(TypeError):
            Rectangle(8, "string", 5, 3, 26)

    def test_13_case_x_string(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 12, "x", 3, 26)

    def test_14_case_y_string(self):
        with self.assertRaises(TypeError):
            Rectangle(8, 12, 5, "y", 26)

    def test_15_case_width_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(-10, 12, 5, 3, 26)

    def test_16_case_height_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(8, -9, 5, 3, 26)

    def test_17_case_x_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(8, 12, -5, 3, 26)

    def test_18_case_y_value_error(self):
        with self.assertRaises(ValueError):
            Rectangle(8, 12, 5, -3, 26)


if __name__ == '__main__':
    unittest.main()
