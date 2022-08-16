# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

src_file = argv[1]
dst_file = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(src_file, 'r') as f, open(dst_file, 'w') as d:
    for line in f:
        if line.startswith('!') == False and ignore[0] not in line and ignore[1] not in line and ignore[2] not in line:
            d.write(line)