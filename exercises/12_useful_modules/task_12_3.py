# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate

reach = ['8.8.8.8', '1.1.1.1'] 
unreach = ['192.168.0.1', '172.16.0.1']

def print_ip_table(reach,unreach):
    addr_dict = {}
    addr_dict['Reachable'] = reach
    addr_dict['Unreachable'] = unreach 
    table = tabulate(addr_dict, headers='keys')
    print(table)


if __name__ == "__main__":
    print_ip_table(reach,unreach)
