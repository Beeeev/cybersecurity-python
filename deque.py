
from collections import deque
d = deque("ghi")

for elem in d:
    print(elem.upper())

d.append("j")
d.appendleft("f")
d.pop()

d.popleft()
print(d)


list()
print(d[0])
print(d[-1])
list(reversed(d))
print("h" in d)
d.extend("jkl")

print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
d.clear()
##d.pop()
d.extendleft("abc")
print(d)
