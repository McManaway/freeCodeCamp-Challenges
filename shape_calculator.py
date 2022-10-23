# Shape Calculator Challenge for freeCodeCamp Course
# "Scientific Computing with Python"
# Author: Blake McManaway
# GitHub: McManaway
# ------------------------------------------------------------------- #
import unittest


class Rectangle:

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def set_width(self, new_width: float)-> None:
        self.width = new_width

    def set_height(self, new_height: float) -> None:
        self.height = new_height

    def get_area(self) -> float:
        return self.width*self.height

    def get_perimeter(self) -> float:
        return 2*self.width + 2*self.height

    def get_diagonal(self) -> float:
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        picture = ""
        for i in range(self.height):
            picture += "*"*self.width + "\n"
        return picture

    def get_amount_inside(self, other) -> float:
        vert_num = self.height // other.height
        hor_num = self.width // other.width
        return vert_num*hor_num

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class Square (Rectangle):

    def __init__(self, side: float):
        self.width = side
        self.height = side
        self.side = side

    def set_side(self, new_side: float) -> None:
        self.width = new_side
        self.height = new_side
        self.side = new_side

    def set_width(self, new_width: float) -> None:
        self.set_side(new_width)

    def set_height(self, new_height: float) -> None:
        self.set_side(new_height)

    def __str__(self) -> str:
        return f"Square(side={self.side})"


# TESTING
# -------------------------------------------------------------------- #


class UnitTests(unittest.TestCase):
    maxDiff = None

    def setUp(self):
        self.rect = Rectangle(3, 6)
        self.sq = Square(5)

    def test_rectangle_string(self):
        actual = str(self.rect)
        expected = "Rectangle(width=3, height=6)"
        error_message = 'Expected string representation of rectangle' \
                        'to be "Rectangle(width=3, height=6)"'
        self.assertEqual(actual, expected, error_message)

    def test_square_string(self):
        actual = str(self.sq)
        expected = "Square(side=5)"
        error_message = 'Expected string representation of square' \
                        'to be "Square(side=5)"'
        self.assertEqual(actual, expected, error_message)

    def test_area(self):
        actual = self.rect.get_area()
        expected = 18
        self.assertEqual(actual, expected, 'Expected area of rectangle'
                                           'to be 18')
        actual = self.sq.get_area()
        expected = 25
        self.assertEqual(actual, expected, 'Expected area of square to'
                                           'be 25')

    def test_perimeter(self):
        actual = self.rect.get_perimeter()
        expected = 18
        self.assertEqual(actual, expected, 'Expected perimeter of'
                                           'rectangle to be 18')
        actual = self.sq.get_perimeter()
        expected = 20
        self.assertEqual(actual, expected, 'Expected perimeter of'
                                           'square to be 20')

    def test_diagonal(self):
        actual = self.rect.get_diagonal()
        expected = 6.708203932499369
        error_message = 'Expected diagonal of rectangle to be' \
                        '6.708203932499369'
        self.assertEqual(actual, expected, error_message)
        actual = self.sq.get_diagonal()
        expected = 7.0710678118654755
        error_message = 'Expected diagonal of square to be' \
                        '7.0710678118654755'
        self.assertEqual(actual, expected, error_message)

    def test_set_attributes(self):
        self.rect.set_width(7)
        self.rect.set_height(8)
        self.sq.set_side(2)
        actual = str(self.rect)
        expected = "Rectangle(width=7, height=8)"
        error_message = 'Expected string representation of rectangle' \
                        'after setting new values to be' \
                        '"Rectangle(width=7, height=8)"'
        self.assertEqual(actual, expected, error_message)
        actual = str(self.sq)
        expected = "Square(side=2)"
        error_message = 'Expected string representation of square' \
                        'after setting new values to be' \
                        '"Square(side=2)"'
        self.assertEqual(actual, expected, error_message)
        self.sq.set_width(4)
        actual = str(self.sq)
        expected = "Square(side=4)"
        error_message = 'Expected string representation of square' \
                        'after setting width to be "Square(side=4)"'
        self.assertEqual(actual, expected, error_message)

    def test_rectangle_picture(self):
        self.rect.set_width(7)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "*******\n*******\n*******\n"
        error_message = 'Expected rectangle picture to be different.'
        self.assertEqual(actual, expected, error_message)

    def test_square_picture(self):
        self.sq.set_side(2)
        actual = self.sq.get_picture()
        expected = "**\n**\n"
        error_message = 'Expected square picture to be different.'
        self.assertEqual(actual, expected, error_message)

    def test_big_picture(self):
        self.rect.set_width(51)
        self.rect.set_height(3)
        actual = self.rect.get_picture()
        expected = "Too big for picture."
        error_message = 'Expected message: "Too big for picture."'
        self.assertEqual(actual, expected, error_message)

    def test_get_amount_inside(self):
        self.rect.set_height(10)
        self.rect.set_width(15)
        actual = self.rect.get_amount_inside(self.sq)
        expected = 6
        error_message = 'Expected `get_amount_inside` to return 6.'
        self.assertEqual(actual, expected, error_message)

    def test_get_amount_inside_two_rectangles(self):
        rect2 = Rectangle(4, 8)
        actual = rect2.get_amount_inside(self.rect)
        expected = 1
        error_message = 'Expected `get_amount_inside` to return 1.'
        self.assertEqual(actual, expected, error_message)

    def test_get_amount_inside_none(self):
        rect2 = Rectangle(2, 3)
        actual = rect2.get_amount_inside(self.rect)
        expected = 0
        error_message = 'Expected `get_amount_inside` to return 0.'
        self.assertEqual(actual, expected, error_message)


if __name__ == "__main__":
    unittest.main()
