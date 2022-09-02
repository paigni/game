import random
import sys
from interface import start_hero_choice
from service import list_from_api
from check import check_hero_energy,is_valid_user_input


hero_name = start_hero_choice()
list_of_monsters = list_from_api()
while True:
    monster_name = random.choice(list_of_monsters)
    random_exp = random.randint(10, 50)
    monster_chance = random.randint(50, 90)
    hero_chance = hero_name.hero_chance()
    hero_energy = hero_name.current_energy
    if check_hero_energy(hero_energy):
        hero_choice = int(input(f'Битва с монстром {monster_name},получаемый опыт за убийство {random_exp},'
                                f'шанс победы {monster_chance},если хотите драться нажмите 1,'
                                f'убежать нажмите 2,закончить игру нажмите 3\n'))
        if is_valid_user_input(hero_choice):
            if hero_choice == 1:
                result_of_fight = hero_name.hero_choice_is_fight(monster_chance,
                                                                 hero_chance,
                                                                 monster_name,
                                                                 random_exp,
                                                                 )
                while not result_of_fight:
                    hero_choice = int(input())
                    if is_valid_user_input(hero_choice):

                        if hero_choice == 1:
                            monster_chance = random.randint(50, 90)
                            hero_chance = hero_name.hero_chance()
                            result_of_fight = hero_name.hero_choice_is_fight(monster_chance,
                                                                             hero_chance,
                                                                             monster_name,
                                                                             random_exp,
                                                                             )
                        if hero_choice == 2:
                            break
                        if hero_choice == 3:
                            sys.exit('Вы вышли из игры')
            elif hero_choice == 2:
                hero_name.hero_choice_is_leave()
                continue
            elif hero_choice == 3:
                sys.exit('Игра завершена')
    else:
        print('У вас недостаточно энергии,зайдите позже')

