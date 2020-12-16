import pandas as pd

COUNTRY_TOP_5 = '1'
COUNTRY_COMPARISON = '2'
EXIT = '3'
OVERALL_RANK = 'a'
GDP_CHOICE = 'b'
SOCIAL_SUPPORT_CHOICE = 'c'

SCORE_COL = 'Score'
GDP_COL = 'GDP per capita'
SOCIAL_SUPPORT_COL = 'Social support'
HEALTH_COL = 'Healthy life expectancy'
FREEDOM_COL = 'Freedom to make life choices'
GENEROSITY_COL = 'Generosity'
CORRUPTION_COL = 'Perceptions of corruption'


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
        if user_second_choice not in [OVERALL_RANK, GDP_CHOICE, SOCIAL_SUPPORT_CHOICE]:
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
        elif user_second_choice == GDP_CHOICE:
            get_data_gdp()
        elif user_second_choice == SOCIAL_SUPPORT_CHOICE:
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


def comparison(df, column, first_index, second_index, first_choice, second_choice):
    first_value = round(df.loc[first_index, column], 4)
    second_value = round(df.loc[second_index, column], 4)

    if first_value > second_value:
        print(f'{column} in', first_choice, 'is', first_value, f'and it is higher than {column} in',
              second_choice, '(', second_value, ')')
    elif first_value < second_value:
        print(f'{column} in', first_choice, 'is', first_value, f'and it is lower than {column} in',
              second_choice, '(', second_value, ')')
    else:
        print('Both countries have similar rating')


def country_comparison():
    df = pd.read_csv('2019.csv')
    while True:
        first_country_choice = input('\nВведите название первой страны для сравнения (на английском языке): ')
        second_country_choice = input('Введите название первой страны для сравнения (на английском языке): ')

        first_country_choice = first_country_choice.title()
        second_country_choice = second_country_choice.title()
        countries = list(df['Country or region'])

        if first_country_choice not in countries:
            print('Страны', first_country_choice, 'нет в списке')
        elif second_country_choice not in countries:
            print('Страны', second_country_choice, 'нет в списке')
        else:
            first_country = df.loc[df['Country or region'] == first_country_choice].index[0]
            second_country = df.loc[df['Country or region'] == second_country_choice].index[0]
            # print(first_country, second_country)

            comparison(df, SCORE_COL, first_country, second_country, first_country_choice, second_country_choice)

            comparison(df, GDP_COL, first_country, second_country, first_country_choice, second_country_choice)

            comparison(df, SOCIAL_SUPPORT_COL, first_country, second_country, first_country_choice,
                       second_country_choice)

            comparison(df, HEALTH_COL, first_country, second_country, first_country_choice, second_country_choice)

            comparison(df, FREEDOM_COL, first_country, second_country, first_country_choice, second_country_choice)

            comparison(df, GENEROSITY_COL, first_country, second_country, first_country_choice, second_country_choice)

            comparison(df, CORRUPTION_COL, first_country, second_country, first_country_choice, second_country_choice)

            break


input_data()
