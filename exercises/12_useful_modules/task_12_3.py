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


avaiable_ip_list = ['8.8.8.8', '127.0.12.12']
unavailable_ip_list = ['115.115.115.115', '192.55.13.4']

def print_ip_table(reach, unreach):
    ips = {'Reachable': reach, 'Unreachable': unreach}
    return(tabulate(ips, headers='keys'))


if __name__ == '__main__':
    print(print_ip_table(avaiable_ip_list, unavailable_ip_list))