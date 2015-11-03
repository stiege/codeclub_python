

def return_divide_by_two(val):
    return val / 2


def return_hello_world():
    return "Hello world"


def return_nth_fibonacci(n):
    i = 1
    j = 1
    start = n
    next_val = 1
    while start > 2:
        next_val = i + j
        j = i
        i = next_val
        start = start - 1
    return next_val


def return_a_duck():

    class Duck(object):

        """A bird, can eat various things"""

        def __init__(self):
            super(Duck, self).__init__()

        def eat(self, item):
            print(item.consume())

        def quack(self):
            return "quack"

        def walk(self):
            return "waddle, waddle, waddle"

    return Duck()
