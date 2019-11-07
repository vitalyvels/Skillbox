# coding=utf-8
# Функция поиска подстроки в строке
# НЕ допускать к регистрации мейлы с определенными символами, словами или их комбинациями
# Импорт функции из другого файла
#Вариант 1
print ('Case 1')
from Helper03Functions import check_symbols
import os

print(os.name)

username = 'dfsdf$hp1qqq'
email = 'wer@gf.com'

if check_symbols(['#','$','%'], s=username):
    print ('username has restricted symbols')
else:
    print ('username Ok')
if check_symbols(restricted_symbols=['#', '$', '%'], s=email):
    print ('email has restricted symbols')
else:
    print ('email Ok')


#Вариант 2
print ('Case 2')
import Helper03Functions
from os import name

print(os.name)

username = 'dfsdf$hp1qqq'
email = 'wer@gf.com'

if Helper03Functions.check_symbols(['#','$','%'], s=username):
    print ('username has restricted symbols')
else:
    print ('username Ok')
if Helper03Functions.check_symbols(restricted_symbols=['#', '$', '%'], s=email):
    print ('email has restricted symbols')
else:
    print ('email Ok')
