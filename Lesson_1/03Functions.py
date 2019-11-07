# coding=utf-8
# Функция поиска подстроки в строке
# НЕ допускать к регистрации мейлы с определенными символами, словами или их комбинациями

def check_symbols(restricted_symbols, s): #Опредление функции проверки символов
    for symb in restricted_symbols:
        if symb in s:
            return True
    return False

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


# if '#' in username:
#     print ('username has restricted symbols')
# if '$' in username:
#     print ('username has restricted symbols')
# if '%' in username:
#     print ('username has restricted symbols')
#
# if '#' in email:
#     print ('email has restricted symbols')
# if '$' in email:
#     print ('email has restricted symbols')
# if '%' in email:
#     print ('email has restricted symbols')