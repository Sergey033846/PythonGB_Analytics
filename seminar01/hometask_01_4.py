# ДЗ 4
# Найдите выручку компании
# Найдите выручку компании в зависимости от месяца.
# Для этого напишите функцию calc_income_by_month(), которая на вход принимает список с датами и список с выручкой, 
# а на выходе словарь, где ключи - это месяцы, а значения - это выручка. Используйте аннотирование типов.

# Пример

# На входе:
# dates = ['2021-11-01']
# incomes = [100]

# После вашего кода будет автоматически добавлено:
# print(calc_income_by_month(dates = ['2021-11-01'], incomes = [100]))

# На выходе:
# {'11': 100}


def calc_income_by_month(dates: list, incomes: list) -> float:
    result = dict()
    
    for i in range(len(dates)):
        month = dates[i][5:7]
        result[month] = result.get(month, 0) + incomes[i]

    return result


print(calc_income_by_month(dates = ['2021-11-01', '2022-11-03'], incomes = [100, 450]))


# решение автотеста
