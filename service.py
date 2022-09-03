import requests
import random
import json
from check import check_is_up_url
import sys
from datetime import datetime, date
from Hero_class import Hero



def list_from_api():
    rand_page = random.randint(1, 5)
    api_url = f'https://ragnarokapi.bravan.cloudns.cl/monsters/?page={rand_page}&limit=100'
    res = requests.get(api_url)
    check_is_up_url(res)
    resp = res.json()
    list_of_monsters = []
    for value in resp:
        name_of_monster = value.get('name').get('en')
        list_of_monsters.append(name_of_monster)
        return list_of_monsters
    if not check_is_up_url(res):
        sys.exit('Монстры недоступны,ведутся технические работы,попробуйте позже')


def date_to_num():
    dt_time = date.today()
    return int(10000 * dt_time.year + 100 * dt_time.month + dt_time.day)


def time_to_num():
    time_str = str(datetime.now().time())
    hh, mm, ss = map(float, time_str.split(':'))
    return int(ss + 60 * (mm + 60 * hh))


def data_hero(name):
    with open(f'{name}.json', 'r+') as readfile:
        text = json.load(readfile)

    hero_names = Hero(text['hero_name'])
    hero_names.max_energy = text['max_energy']
    if date_to_num() - text['time'][1] >= 1 or time_to_num() - text['time'][0] >= 1800:
        hero_names.current_energy = int(hero_names.max_energy)
    else:
        hero_names.current_energy = text['current_energy']
    hero_names.exp = text['exp']
    hero_names.lvl = text['lvl']
    hero_names.exp_to_up_lvl = text['exp_to_up_lvl']
    hero_names.monsters = text['monsters']
    return hero_names
