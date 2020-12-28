import re

with open('people.txt', 'r', encoding='UTF8') as file:
    people_data = file.read()

    pattern_name = re.compile(r'^[A-Z][a-z]+\s[A-Z][a-z]+',re.MULTILINE)
    matches_name = pattern_name.finditer(people_data)
    for name in matches_name:
        print(name)

    pattern_address = re.compile(r'[0-9]{3} .*$',re.MULTILINE)
    matches_address = pattern_address.finditer(people_data)
    for address in matches_address:
        print(address)