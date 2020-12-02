some_text = input('Please enter some text: ')
text = list(some_text)
print(text)

if text == text[::-1]:
    print('This text is palindrome')
else:
    print('This is not palindrome')