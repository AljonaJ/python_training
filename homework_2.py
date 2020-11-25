try:
    personal_code = str(int(input('Please enter your personal code:\n')))  # строка преобразуется в число для проверки,
    # что пользователь ввёл число

    while len(personal_code) != 11:
        print('Personal code length is wrong.')
        personal_code = str(int(input('Please enter valid personal code:\n')))

    if personal_code[0] == '2' or personal_code[0] == '4' or personal_code[0] == '6':
        print(
            'You are woman. Your birthday is ',
            personal_code[5:7], '.', personal_code[3:5], '.', personal_code[1:3],
            sep=''
        )
    elif personal_code[0] == '1' or personal_code[0] == '3' or personal_code[0] == '5':
            print(
                'You are man. Your birthday is ',
                personal_code[5:7], '.', personal_code[3:5], '.', personal_code[1:3],
                sep=''
            )
    else:
        print('Something is wrong. Please check your personal code.')

except ValueError:
    print('Entered personal code consists letters or symbols.')