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
import subprocess as sp


#test

ip_list = ['8.8.8.8', '192.168.0.1', '1.1.1.1', '172.16.0.1']

def ping_ip_addresses(ip_list):
    available_ips = []
    undreach = []
    for ip in ip_list:
        reply = sp.run(['ping', '-c', '3', '-n', ip], stdout=sp.DEVNULL, stderr=sp.DEVNULL)
        if reply.returncode == 0:
            available_ips.append(ip)
        else:
            undreach.append(ip)
    return available_ips, undreach

if __name__ == "__main__":
    result = ping_ip_addresses(ip_list)
    print(result)