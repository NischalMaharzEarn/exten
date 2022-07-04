from sqlalchemy import true


GRAVITY_CONSTANT=9.8
print(GRAVITY_CONSTANT)
GRAVITY_CONSTANT=9.7
print(GRAVITY_CONSTANT)
a = True
print(type(a + a + a))
print(id(a))
a = 5
print(id(a))
b = a
print(id(b))
c = 5
print(id(c))