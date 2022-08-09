# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]


interface_mode = input('Введите режим работы интерфейса (access/trunk): ')
interface_type = input('Введите тип и номер интерфейса: ')

template = {
    "access": access_template,
    "trunk": trunk_template
}

vlan_type = {
    "access": 'Введите номер VLAN: ',
    "trunk": 'Введите разрешенные VLANы:'
}

vlan = input(vlan_type[interface_mode])

print(f'interface {interface_type}')
print('\n'.join(template[interface_mode]).format(vlan))