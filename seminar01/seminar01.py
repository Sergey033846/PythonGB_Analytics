# Задание 1.
# 1.1 Соедините два словаря в один
# 1.2 Напишите функцию, которая на вход принимает два словаря и возвращает один объединенный словарь. Используйте аннотирование типов

# def dicts_union(dict1: dict, dict2: dict) -> dict:
#     # dict3 = dict()
#     # dict3.update(dict1)
#     # dict3.update(dict2)
#     dict3 = {**dict1, **dict2}      # или так
#     return dict3

# dict1 = {'One': 1, 'Two': 2, 'Three': 3}
# dict2 = {'Four': 4, 'Five': 5, 'Six': 6}

# print(f'{dicts_union(dict1, dict2) = }')
# print(f'{dict1 = }')
# print(f'{dict2 = }')
# -----------------------------------------------------

# Задание 2.
# Напишите функцию, которая из двух списков, делает один словарь, где элементы из первого списка - ключи,
# а элементы из второго списка -значения
# Используйте аннотирование типов
# 2.1 Используя цикл for
# 2.2 Используя dict comprehensions

# def dict_create(keys: list, values: list, mode: int=1) -> dict:
#     if mode == 1:
#           result = dict()
#           for i in range(min(len(keys), len(values))):
#             result[keys[i]] = values[i]
#           return result
#     elif mode == 2:
#         return {keys[i]: values[i] for i in range(min(len(keys), len(values)))}

# keys = ['One', 'Two', 'Three']
# values = [1, 2, 3]

# print(f'Using for: ', dict_create(keys, values))
# print()
# print(f'Using dict comprehensions: ', dict_create(keys, values, 2))
# -----------------------------------------------------

# Задание 3.
# Извлеките только два ключа name и age из представленного словаря
# 3.1 Напишите функцию с циклом for
# Функция на вход принимает:
# - исходный словарь
# - ключи, которые нужно извлечь (аргумент по умолчанию)
# На выходе словарь с нужными ключами
# Используйте аннотирование типов
# 3.2 Используя dict comprehensions

# def extract_two_keys(src_dict: dict, keys: list=['name', 'age'], mode: int=1) -> dict:
#     if mode == 1:
#           result = dict()
#           for key in keys:
#             result[key] = client_dict[key]
#           return result
#     elif mode == 2:
#         return {key: client_dict[key] for key in keys}

# client_dict = {
#     'name': 'John',
#     'age': 25,
#     'salary': 5000,
#     'city': 'Moscow'
# }

# print(f'Using for: ', extract_two_keys(client_dict))
# print()
# print(f'Using dict comprehensions: ', extract_two_keys(client_dict, mode=2))
# -----------------------------------------------------

# Задание 4.
# 4.1 Сгенерируйте случайные целые числа от 0 до 100 в количестве 5 штук с помощью модуля random
# ● Зафиксируйте псевдогенерацию, чтобы сгенерированные значения всегда были одинаковые
# ● Используйте list comprehensions
# 4.2 Напишите генератор
# Генератор на вход принимает список с данными о клиенте (данные из пункта 4.1)
# Внутри генератора реализуйте обход по списку с данными
# На каждой итерации генератор будет возвращать кортеж из двух элементов:
# 1. данные по клиенту (в зависимости от итерации, на 0 итерации вернется 0 элемент, на 1 итерации вернется 1 элемент и тд)
# 2. целочисленное значение, которое показывает, сколько секунд прошло с предыдущей итерации
# Примечание: секунды, которые возвращаются должны показывать время не с начала запуска генератора,
# а именно то время, которое прошло с предыдущей итерации.
# А значит время на первой итерации должно равняться 0.
# Используйте функцию time из модуля time для подсчета времени.
# Чтобы проверить работу таймера, запустите проход по генератору в цикле с time.sleep(2)


# import random as rnd
# import time

# def my_generator(client_data: list):
     # time_prev = time.time()
     # for data in client_data:                
        # curr_time = time.time()              
        # yield (data, curr_time - time_prev)   
        # time_prev = curr_time     

# rnd.seed(14)
# random_list = [rnd.randint(0, 100) for _ in range(5)]
# print(f'{random_list = }')

# for i, value in enumerate(my_generator(random_list)):
#     print(f'{i = }, {value = }')
#     time.sleep(2)
# -----------------------------------------------------

# Задание 6.
# Напишите функцию, которая может принимать любое количество трат пользователя и считать сумму и среднее.
# На вход поступают целочисленные значения в любом количестве
# На выходе словарь с ключами суммы трат и средней траты

# def calc_expenses(expenses: list) -> dict:    
#     total_expenses = sum(expenses)
#     return {'total_expenses': total_expenses, 'avg_expenses': total_expenses / len(expenses)}

# list1 = [ 5, 10, 15, 20 ]

# print(f'{calc_expenses(list1) = }')