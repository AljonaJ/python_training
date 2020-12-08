some_text = (input('Please enter some text: ')).lower()
text = some_text.replace(' ', '')
print(text)

if text == text[::-1]:
    print('This text is palindrome')
else:
    print('This is not palindrome')