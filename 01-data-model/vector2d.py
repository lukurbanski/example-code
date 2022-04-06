from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        #return 'Vector(%r, %r)' % (self.x, self.y)
        return 'Vector({}, {})'.format(self.x,self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)


def mypow(x,y):
    n = 1
    for i in range(y): 
        n=x*n
    return n 
 
print(mypow(2,4))

v1 = Vector(1,5)
v2 = Vector(3,8)
v3 = Vector(2,2)


print(v1 * v2 * v3)
print(v1 + v2)
print(v1)

s = 'rabarbar'
print(s.count('r'))

x = 1
while x <= 1000:
    x *= 2
    print(x)

x = "okok"
y = "okok"

if x is y:
    print("ok")