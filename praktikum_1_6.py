list_example = input('Enter random numbers: ').split()
new_list = []

for num in list_example:
    if list_example.count(num) > 1 and num not in new_list:
        new_list.append(num)
print(new_list)
