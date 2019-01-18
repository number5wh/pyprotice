from collections import namedtuple


Point = namedtuple('Point', ('x', 'y', 'z'))

a = Point(1, 2, 3)
print(a.x)
