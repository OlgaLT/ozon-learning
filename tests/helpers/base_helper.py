import string
import random


def string_generator(case, size):
    if case == 'low':
        return ''.join(random.choice(string.ascii_lowercase + string.whitespace) for _ in range(size))
    elif case == 'upper':
        return ''.join(random.choice(string.ascii_uppercase + string.whitespace) for _ in range(size))
    elif case == 'digits':
        return ''.join(random.choice(string.digits) for _ in range(size))
    elif case == 'cyrillic':
        return ''.join(random.choice('абвгдежзийклмнопрстуфхцчшщъыьэюя') for _ in range(size))


def get_group_ids_list(engine):
    row = engine.execute("SELECT id FROM groups WHERE removed IS NOT true")
    ids_list = []
    for r in row:
        ids_list.append(r['id'])
    ids_list = [int(id) for id in ids_list]
    return ids_list


def get_max_id(engine):
    ids_list = get_group_ids_list(engine)
    max_id_in_db = max(ids_list)
    return max_id_in_db


def get_removed_id(engine):
    row = engine.execute("SELECT id FROM groups WHERE removed IS true")
    ids_list = []
    for r in row:
        ids_list.append(r['id'])
    ids_list = [int(id) for id in ids_list]

    return ids_list
