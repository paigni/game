import sys
from Hero_class import Hero
from check import is_valid_user_input
from service import data_hero


def start_hero_choice():
    user_input = 4
    while not is_valid_user_input(user_input):
        user_input = int(input(f"Добро пожаловать в игру,чтобы начать новую,нажмите 1.\n"
                               f"Чтобы загрузить сохранение нажмите 2.\n"
                               f"Чтобы выйти,нажмите 3.\n"))
        if user_input == 3:
            sys.exit()
        if user_input == 1 or 2:
            name = input("Введите имя вашего героя")
            if user_input == 1:
                hero_names = Hero(name)
                hero_names.save_hero()
                return hero_names
            elif user_input == 2:
                return data_hero(name)