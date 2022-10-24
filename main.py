import os
import funcs

menu_options = {
    0: 'Содержимое папки',
    1: 'Создание папки',
    2: 'Удаление папки',
    3: 'Переход во вложенную папку',
    4: 'Переход в предыдущую папку',
    5: 'Создание файла',
    6: 'Запись текста в файл',
    7: 'Просмотр содержимого файла',
    8: 'Удаление файла',
    9: 'Копирование файла из одной папки в другую',
    10: 'Перемещение файла',
    11: 'Переименование файла',
    12: 'Выход'
}

def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def main():
    dir_folder = input('Вы запустили файловый менеджер. Пропишите директорию папки, с которой планируете работать.\n')
    while not os.path.isdir(dir_folder):
        print('Введен неверный путь к папке')
        dir_folder = input('Попробуйте заново. Выберите директорию папки, с которой планируете работать.\n')
    print('Папка выбрана успешно.')
    os.chdir(dir_folder) #изменение директории
    while (True):
        print(f'Текущаю директория: {os.getcwd()}')
        print_menu()
        option = ''
        try:
            option = int(input('Выберите нужную опцию: '))
        except:
            print('Неправильный ввод. Пожалуйста введите число ...')
        if option == 0:
            funcs.listdir()
        elif option == 1:
            name = input('Введите название папки: ')
            funcs.create_new_folder(name)
        elif option == 2:
            name = input('Введите название папки: ')
            funcs.delete_folder(name)
        elif option == 3:
            name = input('Введите название папки: ')
            funcs.open_folder(name)
        elif option == 4:
            funcs.previuos_dir(dir_folder)
        elif option == 5:
            name = input('Введите название файла: ')
            funcs.create_file(name)
        elif option == 6:
            name = input('Введите название файла: ')
            text = input('Введите текст для записи: ')
            funcs.text_entry(name, text)
        elif option == 7:
            name = input('Введите название файла: ')
            funcs.view_file(name)
        elif option == 8:
            name = input('Введите название файла: ')
            funcs.delete_file(name)
        elif option == 9:
            name = input('Введите название файла: ')
            new_dir = input('Введите название новой директории: ')
            funcs.copy_file(name, new_dir)
        elif option == 10:
            name = input('Введите название файла: ')
            new_dir = input('Введите название новой директории: ')
            funcs.replace_file(name, new_dir)
        elif option == 11:
            name = input('Введите название файла, который хотите переименовать: ')
            new_name = input('Введите новое название файла: ')
            funcs.rename_file(name, new_name)
        elif option == 12:
            print('Спасибо за использование программы.')
            exit()
        else:
            print('Недопустимая опция. Пожалуйста введите число от 0 до 12.')

if __name__ == '__main__':
    main()
