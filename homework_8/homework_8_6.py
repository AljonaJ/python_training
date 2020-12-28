import re

personal_code = '''
39008310042 g, 48911216890,
a39007120010
39008317016
390071200106
39007120010
'''
pattern = re.compile(r'\b([1-6])([0-9][0-9])([0-1][0-9])([0-2][0-9]|[3][01?])([0-9][0-9][0-9])([0-9])\b')
matches = pattern.finditer(personal_code)
for match in matches:
    print(match)
