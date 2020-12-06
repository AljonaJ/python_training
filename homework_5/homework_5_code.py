from os import listdir

PROCESS_SINGLE_FILE = '1'
PROCESS_FOLDER = '2'
EXIT = '3'


def menu():
    print('1. Обработать один файл')
    print('2. Обработать все файлы в директории')
    print('3. Выйти\n')


def process_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        file_content = file.read()
    clean_content = ''
    for symbol in file_content:
        if symbol.isalnum() or symbol == ' ':
            clean_content = clean_content + symbol

    words = clean_content.lower().split(' ')
    words_count = len(words)

    uniq_words = set(words)
    uniq_words_count = len(uniq_words)

    if file_name[-4:] == '.txt':
        file_name = file_name[:-4] + '_copy.txt'
    else:
        file_name = file_name + '_copy.txt'
    new_file_content = ', '.join(uniq_words)
    with open(file_name, 'w', encoding='utf-8') as new_file:
        new_file.write(new_file_content)

    return words_count, uniq_words_count
    # print(words_count, uniq_words_count)


def run():
    menu()
    while True:
        user_choice = input('Пожалуйста, введите номер действия: ')
        if user_choice == EXIT:
            print('Хорошего дня!')
            exit()
        elif user_choice == PROCESS_SINGLE_FILE:
            while True:
                try:
                    file_name = input('Введите название файла: ')
                    words_count, uniq_words_count = process_file(file_name)
                    print('Данный текст содержит', words_count, 'слов и', uniq_words_count, 'уникальных слов.')
                    print('Создан новый файл', file_name[:-4] + '_copy.txt cо списком уникальных слов.')
                    exit()
                except FileNotFoundError:
                    print('Файл не найден, попробуйте снова')
        elif user_choice == PROCESS_FOLDER:
            while True:
                try:
                    folder_name = input('Введите название папки: ')
                    folder_content = listdir(folder_name)
                    if len(folder_content) == 0:
                        print('Папка пустая, выберите другую')
                    else:
                        for file_name in folder_content:
                            if file_name[-9:] == '_copy.txt':
                                continue
                            file_name = '\\'.join([folder_name, file_name])
                            words_count, uniq_words_count = process_file(file_name)
                            print(file_name, 'содержит', words_count, 'слов и', uniq_words_count, 'уникальных слов.')
                            print('Создан новый файл', file_name[:-4] + '_copy.txt cо списком уникальных слов.')
                            # print(folder_content)
                        exit()
                except FileNotFoundError:
                    print('Папка не найдена, попробуйте снова')
        else:
            print('Такого номера нет, попробуйте снова')


run()
