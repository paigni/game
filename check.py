from os.path import isfile


def check_is_up_url(req):
    if req.status_code == 200:
        return True
    return False


def is_valid_user_input(inp):
    if 1 <= int(inp) <= 3:
        return True
    return False


def check_hero_energy(energy):
    if energy >= 0:
        return True
    return False


def check_is_hero_exists(name):
    opening_file = isfile(name)
    if opening_file:
        return True
    return False
