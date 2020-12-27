tuple_a = (1, 2, 3, 5, 8)
tuple_b = (8, 2, 5)

list_a = list(tuple_a)
list_b = list(tuple_b)

tuple_ab = tuple(list_a + list_b)
print(tuple_ab)

