import re

html_code = '''
<style>
div {
    background-color: #00bfff;
    color: #ffffff;
}
</style>
'''
pattern = re.compile(r'#[a-fA-F0-9]{6}\b')
matches = pattern.finditer(html_code)
for match in matches:
    print(match)