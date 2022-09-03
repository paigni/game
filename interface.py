import sys
from Hero_class import Hero
from check import is_valid_user_input, check_is_hero_exists
from service import data_hero


def start_hero_choice():
    user_input = 4
    while not is_valid_user_input(user_input):
        user_input = int(input(f"Добро пожаловать в игру,чтобы начать новую,нажмите 1.\n"
                               f"Чтобы загрузить сохранение нажмите 2.\n"
                               f"Чтобы выйти,нажмите 3.\n"))
        if user_input == 3:
            sys.exit('Вы вышли из игры')
        elif user_input == 1 or user_input == 2:
            name = input("Введите имя вашего героя")
            if check_is_hero_exists(name) and user_input == 1:
                if user_input == 1:
                    hero_name = Hero(name)
                    hero_name.save_hero()
                    return hero_name
            elif user_input == 2:
                return data_hero(name)
        else:
            print('Неверный ввод')
