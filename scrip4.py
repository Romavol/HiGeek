# Задания 4 урок

from sys import argv

script_name, first_param, second_param = argv

hour = float(first_param)
prem = float(second_param)
tariff = 15  # зададим 1 вручную

print("Cумма зарплаты : ", (hour * 15 + prem))
