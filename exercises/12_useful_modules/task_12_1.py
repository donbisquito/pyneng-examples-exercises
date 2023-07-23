# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

ip_list = ['8.8.8.8', '115.115.115.115', '127.0.12.12', '192.55.13.4']

def ping_ip_addresses(ip_list):
    avalable_ip = []
    unavalable_ip = []
    for ip in ip_list:
        reply = subprocess.run(['ping','-c', '2', '-n', ip], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if reply.returncode == 0:
            avalable_ip.append(ip)
        else:
            unavalable_ip.append(ip)

    return avalable_ip, unavalable_ip


print(ping_ip_addresses(ip_list))

