import pandas as pd

COUNTRY_TOP_5 = '1'
COUNTRY_COMPARISON = '2'
EXIT = '3'
OVERALL_RANK = 'a'
GDP = 'b'
SOCIAL_SUPPORT = 'c'


def menu():
    while True:
        print('1. Вывести топ-5 стран')
        print('2. Сравнить две страны')
        print('3. Выйти\n')
        user_choice = input('Пожалуйста, введите номер действия: ')
        if user_choice not in [COUNTRY_TOP_5, COUNTRY_COMPARISON, EXIT]:
            print('Такого номера нет, попробуйте снова\n')
            continue
        break
    return user_choice


def menu_top_5():
    while True:
        print('a. Общий ранк')
        print('b. ВВП и коррупция')
        print('c. Социальная поддержка и Показатель здоровой жизни\n')
        user_second_choice = input('Пожалуйста, выберите один из вариантов: ')
        if user_second_choice not in [OVERALL_RANK, GDP, SOCIAL_SUPPORT]:
            print('Такого номера нет, попробуйте снова\n')
            continue
        break
    return user_second_choice


def input_data():
    user_choice = menu()
    if user_choice == COUNTRY_TOP_5:
        user_second_choice = menu_top_5()
        if user_second_choice == OVERALL_RANK:
            get_data_overall()
        elif user_second_choice == GDP:
            get_data_gdp()
        elif user_second_choice == SOCIAL_SUPPORT:
            get_data_social_support()
    elif user_choice == COUNTRY_COMPARISON:
        country_comparison()
    elif user_choice == EXIT:
        print('Хорошего дня!')


def get_data_overall():
    df = pd.read_csv('2019.csv', nrows=5)
    pd.set_option('display.max_columns', 9)
    print(df)


def get_data_gdp():
    df = pd.read_csv('2019.csv')
    df = df.sort_values(by=['GDP per capita', 'Score'], ascending=False)
    df = df[['Country or region', 'GDP per capita', 'Perceptions of corruption']][:5]
    print(df.to_string(index=False))


def get_data_social_support():
    df = pd.read_csv('2019.csv')
    df = df.sort_values(by=['Social support', 'Healthy life expectancy'], ascending=False)
    df = df[['Country or region', 'Overall rank', 'Social support', 'Healthy life expectancy']][:5]
    print(df.to_string(index=False))


def country_comparison():
    df = pd.read_csv('2019.csv')
    first_country_choice = input('Введите название первой страны для сравнения (на английском языке): ')
    second_country_choice = input('Введите название первой страны для сравнения (на английском языке): ')
    pass
    # Второй пункт не успела

input_data()
