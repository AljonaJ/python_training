import re

some_string = input()
pattern = re.compile(r'^[A-z0-9]+$')
string_match = pattern.search(some_string)
if string_match:
    print(string_match)
else:
    print('No')

# jmfgcy767fy8o0y67utfgy87h , jytg1
# kjh!?54
# kmk,nbvgf
# agcght6543ukbc
# AFV89 LHV
# AK76bv

