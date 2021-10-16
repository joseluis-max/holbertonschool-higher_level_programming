import unittest
from models.square import Square


class TestSquareMethod(unittest.TestCase):
    def test_00_case_base_success(self):
        new_obj = Square(5)
        self.assertEqual(new_obj.size, 5)

    def test_01_case_all_args_success(self):
        new_obj = Square(15, 4, 7, 15)
        self.assertEqual(new_obj.x, 4)
        self.assertEqual(new_obj.y, 7)
        self.assertEqual(new_obj.size, 15)
        self.assertEqual(new_obj.id, 15)

    def test_02_case_all_args_fail(self):
        with self.assertRaises(TypeError):
            Square(15, 4, "40", 15)
        with self.assertRaises(TypeError):
            Square("15", 4, 40, 15)
        with self.assertRaises(TypeError):
            Square(15, "4", 40, 15)

    def test_03_case_all_args_fail_negatives(self):
        with self.assertRaises(ValueError):
            Square(15, -5, 2, 8)
        with self.assertRaises(ValueError):
            Square(-15, 5, 2, 8)
        with self.assertRaises(ValueError):
            Square(15, 5, -2, 8)

    def test_04_case_size_args_fail_zero(self):
        with self.assertRaises(ValueError):
            Square(0, 0, 0, 8)

    def test_05_case_fail_01_without_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_06_setter_size_height_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.size = 40
        self.assertEqual(new_obj.height, 40)

    def test_07_setter_size_width_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.size = 40
        self.assertEqual(new_obj.width, 40)

    def test_08_setter_size_fail(self):
        new_obj = Square(8, 5, 3, 26)
        with self.assertRaises(ValueError):
            new_obj.size = -8

    def test_09_setter_x_success(self):
        new_obj = Square(8, 5, 3, 26)
        new_obj.x = 40
        self.assertEqual(new_obj.x, 40)


if __name__ == '__main__':
    unittest.main()
