import re
import string
# Записываем совиный в переменную
str_to_conv = input('Введи совиный: ')
# Функция для замены нескольких значений
def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str
# создаем словарь со значениями и строку, которую будет изменять
replace_values = {"У": "0", "Г": "1"}
# изменяем строку
Conv = multiple_replace(str_to_conv, replace_values)
# декодируем
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
# Печатаем
print (decode_binary_string(Conv))





