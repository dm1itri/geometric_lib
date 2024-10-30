from math import pi
from unittest import TestCase
import circle
import rectangle
import square
import triangle


class TestCircle(TestCase):
    def test_area_incorrect_data(self):
        self.assertEqual(circle.area(0), 0)
        self.assertEqual(circle.area("five"), 0)

    def test_area(self):
        self.assertEqual(circle.area(5), pi * 5 * 5)

    def test_perimeter_incorrect_data(self):
        self.assertEqual(circle.perimeter(0), 0)
        self.assertEqual(circle.area("five"), 0)

    def test_perimeter(self):
        self.assertEqual(circle.perimeter(5), 2 * pi * 5)


class TestRectangle(TestCase):
    def test_area_incorrect_data(self):
        self.assertEqual(rectangle.area(0, 5), 0)
        self.assertEqual(rectangle.area('five', 'five'), 0)

    def test_area(self):
        self.assertEqual(rectangle.area(2, 5), 10)

    def test_perimeter_incorrect_data(self):
        self.assertEqual(rectangle.perimeter(0, 5), 0)
        self.assertEqual(rectangle.perimeter('five', 'five'), 0)

    def test_perimeter(self):
        self.assertEqual(rectangle.perimeter(2, 5),14)


class TestSquare(TestCase):
    def test_area_incorrect_data(self):
        self.assertEqual(square.area(0), 0)
        self.assertEqual(square.area('five'), 0)

    def test_area(self):
        self.assertEqual(square.area(5), 25)

    def test_perimeter_incorrect_data(self):
        self.assertEqual(square.perimeter(0), 0)
        self.assertEqual(square.perimeter('five'), 0)

    def test_perimeter(self):
        self.assertEqual(square.perimeter(5), 20)


class TestTriangle(TestCase):
    def test_area_incorrect_data(self):
        self.assertEqual(triangle.area(0, 5), 0)
        self.assertEqual(triangle.area(5, 0), 0)
        self.assertEqual(triangle.area('zero', 'five'), 0)

    def test_area(self):
        self.assertEqual(triangle.area(5, 5), 12.5)

    def test_perimeter_incorrect_data(self):
        self.assertEqual(triangle.perimeter(0, 5, 5), 0)
        self.assertEqual(triangle.perimeter(5, 0, 5), 0)
        self.assertEqual(triangle.perimeter(5, 5, 0), 0)
        self.assertEqual(triangle.perimeter('five', 'five', 'five'), 0)

    def test_perimeter(self):
        self.assertEqual(triangle.perimeter(5, 5, 5), 15)
