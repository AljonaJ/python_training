side_a = int(input('Please enter side a lenght:'))
side_b = int(input('Please enter side b lenght:'))
side_c = int(input('Please enter side c lenght:'))

half_perimeter = (side_a + side_b + side_c) / 2
area = (half_perimeter * (half_perimeter - side_a) * (half_perimeter - side_b) * (half_perimeter - side_c)) ** 0.5

print('Side A = ', side_a, 'Side B =', side_b, 'Side C =', side_c)
print('Area of triangle is equal to', area)