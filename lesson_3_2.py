courses = ['History', 'Math', 'Programming', 'Literature']
numbers = [2, 5, 7, 8, 4, 7, 9]
courses.append('Art')
courses.extend(numbers)  # extend соединит 2 списка (применяется только к спискам (list))
popped_item = courses.pop()  # pop удаляет последний элемент в списке
print(courses)

# for x in range

for x in range(1, 101):  # чет/нечет
    if x % 2 == 0:
        print(x, 'odd')
    else:
        print(x, 'even')