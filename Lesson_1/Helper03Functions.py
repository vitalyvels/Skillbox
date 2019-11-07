# coding=utf-8
# Функция поиска подстроки в строке
# НЕ допускать к регистрации мейлы с определенными символами, словами или их комбинациями
# Вспомогательная функция

def check_symbols(restricted_symbols, s): #Опредление функции проверки символов
    for symb in restricted_symbols:
        if symb in s:
            return True
    return False

