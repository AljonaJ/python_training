import re

time_test = '''
a 13:15
22:49
35:99
21:72
13.15
00:59
8:22
08:25
01:00
122:49
108:25
22:17 h
23:0100
'''
pattern = re.compile(r'\b([01\s][0-9]:[0-5][0-9])\b|\b(2[0-3]:[0-5][0-9])\b')
matches = pattern.finditer(time_test)
for match in matches:
    print(match)