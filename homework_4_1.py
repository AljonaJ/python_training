from datetime import datetime, date


def check_personal_code(personal_code):
    if len(personal_code) != 11:
        return False

    control_number = float(f'{personal_code[0:6]}{personal_code[7:10]}') / 31
    control_number_final = round((control_number - int(control_number)) * 31)

    control_character = personal_code[10]
    control_string = '0123456789ABCDEFHJKLMNPRSTUVWXY'

    return control_character == control_string[control_number_final]


def get_personal_info(personal_code):
    if personal_code[6] == '+':
        century = '18'
    elif personal_code[6] == '-':
        century = '19'
    elif personal_code[6] == 'A':
        century = '20'
    else:
        return False

    birthday_control = personal_code[0:2] + personal_code[2:4] + century + personal_code[4:6]
    birthday_control_format = datetime.strptime(birthday_control, '%d%m%Y')

    gender_number = int(personal_code[7:10]) % 2
    if gender_number == 1:
        gender = 'man'
    else:
        gender = 'woman'

    residence_status = int(personal_code[7:10])
    if 2 <= residence_status <= 899:
        residence = 'You were born in Finland.'
    elif 900 <= residence_status <= 999:
        residence = 'You have temporary personal identification. You are alien :)'
    else:
        return False
    return birthday_control_format, gender, residence


def main():
    message = 'Please enter your personal code:\n'
    error_message = 'Personal code is wrong.'
    while True:
        try:
            personal_code = input(message)
            if check_personal_code(personal_code) is True:
                if get_personal_info(personal_code) is not False:
                    birthday_control_format, gender, residence = get_personal_info(personal_code)
                    break

            print(error_message)
        except ValueError:
            print(error_message)

        message = 'Please enter valid personal code:\n'

    today = date.today()
    age = today.year - birthday_control_format.year

    print('Your personal code is', personal_code + '. You are', gender + '.')
    print('Your birthday is', birthday_control_format.strftime('%d.%m.%Y') + '. You are', age, 'years old.')
    print(residence)


main()
