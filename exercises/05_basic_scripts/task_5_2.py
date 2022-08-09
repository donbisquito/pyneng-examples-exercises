# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

network = input('Введите сеть в формате: 10.1.1.0/24: ')
net = network.split('/')[0].split('.')
mask = network.split('/')[1]
print('''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''.format(int(net[0]),int(net[1]),int(net[2]),int(net[3])))

mask_octets = ("1" * int(mask)) + ("0" * (32 - int(mask)))
first_mask_octet = mask_octets[:8]
second_mask_octet = mask_octets[8:16]
third_mask_octet = mask_octets[16:24]
fourth_mask_octet = mask_octets[24:33]



print('''
Mask:
/{}
{:<10}{:<10}{:<10}{:<10}
{:8}  {:8}  {:8}  {:8}
'''.format(mask, int(first_mask_octet, 2), int(second_mask_octet, 2), int(third_mask_octet, 2), int(fourth_mask_octet, 2), first_mask_octet, second_mask_octet, third_mask_octet, fourth_mask_octet))
