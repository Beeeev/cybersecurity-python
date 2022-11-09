from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(11, y=22)
p = p[0] + p[1]
print(p)
x, y = p
print(x, y)
