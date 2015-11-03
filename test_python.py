import unittest
import random
from make_me import *

n = random.randint(0, 1000)
print(n)

bread_consumed = False


class Bread(object):

    """A chewable carbohydrate"""

    def __init__(self):
        super(Bread, self).__init__()
        self.calories = 24
        self.colour = "brown"

    def consume(self):
        global bread_consumed
        bread_consumed = True
        return "Healthy goodness"


class CodeClub(unittest.TestCase):

    def test_returning_divide_by_two(self):
        a = return_divide_by_two(n)
        self.assertEqual(n / 2, a)

    def test_return_hello_world(self):
        a = return_hello_world()
        if not isinstance(a, str):
            raise Exception("Did not return a string")
        self.assertEqual("hello world", a.lower())

    def test_return_a_duck(self):
        t_duck = return_a_duck()

        # Check the duck sounds like a duck
        self.assertEqual("quack", t_duck.quack())

        # Check the duck walks like a duck
        self.assertEqual("waddle, waddle, waddle", t_duck.walk())

        # Check the duck can eat bread
        test_bread = Bread()
        t_duck.eat(test_bread)
        if not bread_consumed:
            raise Exception("Duck did not eat the bread it was given")

        # Yup, must be a duck.

    def test_return_nth_fibonacci(self):
        a = return_nth_fibonacci(n)
        i = 1
        j = 1
        start = n
        next_val = 1
        while start > 2:
            next_val = i + j
            j = i
            i = next_val
            start = start - 1
        self.assertEqual(a, next_val)


if __name__ == '__main__':
    unittest.main()
