#!/usr/bin/python
# -*- coding: utf-8 -*-
#Задание 3.1

#Обработать строку NAT таким образом,
#чтобы в имени интерфейса вместо FastEthernet было GigabitEthernet.

#Ограничение: Все задания надо выполнять используя только пройденные темы.

nat = 'ip nat inside source list ACL interface FastEthernet0/1 overload'
new_nat =  nat.replace("FastEthernet", "GigabitEthernet")
print(new_nat)

