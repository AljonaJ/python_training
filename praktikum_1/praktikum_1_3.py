# Стороны треугольника
a = float(input('a = '))  # 10
b = float(input('b = '))  # 24
c = float(input('c = '))  # 26

if c**2 == a**2 + b**2:
    print('It is a right triangle')
else:
    print('This is not a right triangle')