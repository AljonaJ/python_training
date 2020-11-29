message = 'Please enter your personal code:\n'
while True:
    try:
        personal_code = input(message)
        int(personal_code)
        if len(personal_code) != 11:
            print('Personal code length is wrong.')
        else:
            check_numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]  # 1 ступень проверки контрольного номера
            check_numbers_2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]  # 2 ступень проверки контрольного номера
            control_sum_1 = 0
            control_sum_2 = 0

            for i in range(0, 10):
                # подсчет суммы для первой ступени проверки
                control_sum_1 = control_sum_1 + int(personal_code[i]) * check_numbers_1[i]
                # подсчет суммы для второй ступени проверки
                control_sum_2 = control_sum_2 + int(personal_code[i]) * check_numbers_2[i]

            # Вычисление контрольного номера
            control_number_1 = control_sum_1 % 11
            control_number_2 = control_sum_2 % 11

            # Если первый контрольный номер меньше 10 и совпадает с последней цифрой введеного личного кода,
            # или если первый контрольный номер равен (больше) 10, но второй контрольный номер совпадает с
            # последней цифрой введеного личного кода, или если второй контрольный номер равен (больше) 10 и
            # последняя цифра введенного личного кода равняется 10, то выходим из цикла
            if (control_number_1 < 10 and int(personal_code[10]) == control_number_1) or (
                    int(personal_code[10]) == control_number_2 or
                    control_number_2 == 10 and int(personal_code[10]) == 0
            ):
                break
            else:
                print('Control code of your personal code is wrong.')
    except ValueError:
        print('Entered personal code consists letters or symbols. Personal code must contain only numbers.')

    message = 'Please enter valid personal code:\n'

gender_control = personal_code[0]
year_control = personal_code[1:3]
month_control = personal_code[3:5]
day_control = personal_code[5:7]
birthplace = int(personal_code[7:10])

if gender_control == '1':
    gender = 'man'
    year = '18'
elif gender_control == '2':
    gender = 'woman'
    year = '18'
elif gender_control == '3':
    gender = 'man'
    year = '19'
elif gender_control == '4':
    gender = 'woman'
    year = '19'
elif gender_control == '5':
    gender = 'man'
    year = '20'
elif gender_control == '6':
    gender = 'woman'
    year = '20'
else:
    gender = ''
    year = ''

print(
    'Your personal code is ' + personal_code + '. You are ' + gender +
    '. Your birthday is ' + day_control + '.' + month_control + '.' + year + year_control
)

if 1 <= birthplace <= 10:
    place = 'Kuressaare Haigla'
elif 11 <= birthplace <= 19:
    place = 'Tartu Ülikooli Naistekliinik'
elif 21 <= birthplace <= 220:
    place = 'Ida-Tallinna Keskhaigla" or "Pelgulinna sünnitusmaja" ' \
            'or Hiiumaa or Keila or "Rapla haigla" or "Loksa haigla'
elif 221 <= birthplace <= 270:
    place = 'Ida-Viru Keskhaigla (Kohtla-Järve)'
elif 271 <= birthplace <= 370:
    place = 'Maarjamõisa Kliinikum (Tartu)" or "Jõgeva Haigla'
elif 371 <= birthplace <= 420:
    place = 'Narva Haigla'
elif 421 <= birthplace <= 470:
    place = 'Pärnu Haigla'
elif 471 <= birthplace <= 490:
    place = 'Pelgulinna Sünnitusmaja (Tallinn)" or "Haapsalu haigla'
elif 491 <= birthplace <= 520:
    place = 'Järvamaa Haigla (Paide)'
elif 521 <= birthplace <= 570:
    place = 'Rakvere", "Tapa haigla'
elif 571 <= birthplace <= 600:
    place = 'Valga Haigla'
elif 601 <= birthplace <= 650:
    place = 'Viljandi Haigla'
elif 651 <= birthplace <= 700:
    place = 'Lõuna-Eesti Haigla (Võru)" or "Põlva Haigla '
else:
    place = 'unknown'
print('You were born in "' + place + '".')
