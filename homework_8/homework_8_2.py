import re

some_text = '''
2*9-6*5
(3+5)-9*4
решить пример (4-2)*2+5
'''
pattern = re.compile(r'\d+[^+]')
matches = pattern.finditer(some_text)
for match in matches:
    print(match)
