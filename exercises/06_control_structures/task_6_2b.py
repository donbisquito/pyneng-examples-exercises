# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_valid = False

while not ip_valid:
    ip_address = input('Введите адрес в формате 10.10.1.1: ')
    octets = ip_address.split('.')
    for octet in octets:
        if len(octets) != 4 or octet.isdigit() == False or int(octet) not in range(256) or '.' not in ip_address or ',' in ip_address:
            print('Неправильный IP-адрес')
            break
        else:
            ip_valid = True
                

if int(octets[0]) > 0 and int(octets[0]) < 223:
    print('unicast')
elif int(octets[0]) > 223 and int(octets[0]) < 239:
    print('multicast')
elif ip_address == '255.255.255.255':
    print('local broadcast')
elif ip_address == '0.0.0.0':
    print('unassigned')
else:
    print('unused')




