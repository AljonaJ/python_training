# # list = ['one', 'two', 'three']
# # print(list[0])
# # print(len(list))
# # print(max(list))  # выйдет two, сортируется в алфавитном порядке (one, three, two)
#
# workers_list = [['John', 1000], ['Alice', 3000], ['Bob', 2500]]
# # print(workers_list[0][0])
# # print(workers_list[::-1])  # выйдет список в обратном порядке
# # workers_list.append(['Daniel', 3500])  # добавить новый элемент в конец списка
# workers_list[1] = ['Daniel', 3500]  # добавить в список в конкретное место (вместо чего-то)
# workers_list.insert(2, ['Daniel', 3500])  # добавить в список в конкретное место
#
# print(workers_list)
#
# workers_list = ['John', '3000', 'Bob', '2500']
# print(max(workers_list))
#
# tuple_example = (1, 2, 3, 5, 7)  # кортеж, параметры нельзя изменять

list_1 = [1, 2, 3, 5, 7]
tuple_1 = (1, 2, 3, 5, 7, 4, 10)
list_2 = list(tuple_1)
tuple_2 = tuple(list_1)
print(list_2)
print(tuple_2)

# some_list = [1, 2, 3, 5, 7, 1, 2, 3, 4, 5, 10]
# some_set = set(some_list)  # при пребразовании list в set повторяющиеся элементы отбрасываются
# print(some_set)
#
# user_value = int(input('Enter some number:'))
# some_set.add(12)  # добавили число 14
# some_set.remove(4)  # удалили число 4 из set'а
# if user_value in some_set:
#     print('Your value is in the set')
# else:
#     print('Your value is not in the set')
# # set (множество) не индексируется, на выход подается каждый раз в произвольном порядке
#
# new_list = [1, 2, 3, 5, 7, 1, 2, 3, 4, 5, 10]
# for x in new_list:
#     print(x)
#     if x == 4:
#         print(x)
#         break