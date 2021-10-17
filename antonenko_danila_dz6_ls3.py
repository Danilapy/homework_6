from itertools import zip_longest
import json


with open('users.txt', 'r', encoding='utf-8') as name,\
    open('hobbies.txt', 'r', encoding='utf-8') as hobby:
        names = name.read().splitlines()
        hobbies = hobby.read().splitlines()

if len(names) < len(hobbies):
        print(1)
else:
        user_hobby = dict(zip_longest(names, hobbies, fillvalue=None))
        with open('users_hobbies_list(3_задание).txt', 'w', encoding='utf-8') as f:
                json.dump(user_hobby, f, ensure_ascii=False)