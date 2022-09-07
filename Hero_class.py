import random
import json
from datetime import date, datetime


class Hero:
    max_energy = 100
    current_energy = max_energy
    exp = 0
    lvl = 1
    exp_to_up_lvl = 100
    monsters = []

    def __init__(self, name):
        self.name = name

    def hero_chance(self):
        return random.randint(10, 100)

    def hero_time(self):
        time_str = str(datetime.now().time())
        hh, mm, ss = map(float, time_str.split(':'))
        return int(ss + 60 * (mm + 60 * hh))

    def hero_date(self):
        dt_time = date.today()
        return int(10000 * dt_time.year + 100 * dt_time.month + dt_time.day)

    def save_hero(self):
        data = {
            'hero_name' : self.name,
            'max_energy': self.max_energy,
            'current_energy': self.current_energy,
            'exp': self.exp,
            'lvl': self.lvl,
            'exp_to_up_lvl': self.exp_to_up_lvl,
            'monsters': self.monsters,
            'time': [self.hero_time(), self.hero_date()]
        }
        with open(f'{self.name}.json', 'w+') as outfile:
            json.dump(data, outfile)

    def update_lvl(self):
        self.exp = self.exp - self.exp_to_up_lvl
        self.lvl += 1
        self.exp_to_up_lvl *= 1.5
        self.max_energy *= 1.2
        print(
            f'Повышение уровня! Ваш текущий уровень {self.lvl}текущий опыт {self.exp}\n'
            f'для повышения уровня нужно набрать {self.exp_to_up_lvl} очков'
            )

    def update_exp_and_check_lvl(self, ran_exp):
        self.exp += ran_exp
        print(f'Герой победил,получено {ran_exp} опыта')
        if self.exp >= self.exp_to_up_lvl:
            self.update_lvl()

    def hero_choice_is_fight(self, m_chance, h_chance, monsters_name,random_exp):
        self.current_energy -= 10
        print(f'Ваша текущая энергия {self.current_energy}')
        if m_chance < h_chance:
            print(f'Монстр победил,хотите повторно испытать удачу?\n'
                  f'Если да,то нажмите 1,если не сегодня 2,выйти из игры 3')
            return False

        self.update_exp_and_check_lvl(random_exp)
        self.monsters.append(monsters_name)
        self.save_hero()
        return True

    def hero_choice_is_leave(self):
        self.current_energy -= 3
        self.save_hero()
        print(f'Ваша текущая энергия {self.current_energy}')
