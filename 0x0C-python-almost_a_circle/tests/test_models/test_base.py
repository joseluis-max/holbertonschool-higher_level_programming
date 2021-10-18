import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestBaseMethods(unittest.TestCase):
    def test_01_case_instance_Square_success(self):
        new_obj1 = Square(5)
        self.assertIsInstance(new_obj1, Rectangle)

    def test_01_case_instance_fail_01(self):
        new_obj1 = {"size": 5}
        self.assertIsNot(new_obj1, (Rectangle, Square))

    def test_01_case_instance_fail_02(self):
        new_obj1 = {"width": 5, "height": 13}
        self.assertIsNot(new_obj1, (Rectangle, Square))

    def test_02_type_from_json_string_success(self):
        new_obj = Rectangle(2, 3)
        to_string = '[{"id": 1, "width": 10, "_Rectangle__height": 7, "_Rectangle__x": 2, "_Rectangle__y": 8}, ' \
                    '{"id": 2, "_Rectangle__width": 2, "_Rectangle__height": 4, "_Rectangle__x": 0, ' \
                    '"_Rectangle__y": 0}]'
        result = new_obj.from_json_string(to_string)
        self.assertEqual(type(result), list)

    def test_03_create_square_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsInstance(new_obj2, Square)

    def test_03_create_rectangle_success(self):
        new_obj1 = Rectangle(5, 2)
        dictionary = {"width": 10, "height": 5, "x": 2, "y": 2}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsInstance(new_obj2, Rectangle)

    def test_03_create_square_fail(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsNot(new_obj2, Rectangle)

    def test_03_create_rectangle_fail(self):
        new_obj1 = Rectangle(5, 2)
        dictionary = {"width": 10, "height": 5, "x": 2, "y": 2}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertIsNot(new_obj2, Square)

    def test_04_create_size_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        self.assertEqual(new_obj2.size, 10)

    def test_04_create_x_success(self):
        new_obj1 = Square(5)
        dictionary = {"size": 10}
        new_obj2 = new_obj1.create(**dictionary)
        new_obj2.x = 15
        self.assertEqual(new_obj2.x, 15)


if __name__ == '__main__':
    unittest.main()
