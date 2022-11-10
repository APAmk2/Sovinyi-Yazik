import re
import string
# Создаём переменную и записываем в неё текст
str_to_conv = input('Введи текст: ')
# Выводим строку которую переведём (Дебаг)
print("Вот эту строку переведём на совиный 2.0: ",str_to_conv) 
# Конвертируем текст в двоичный код 
bin_result = ''.join(format(ord(x), '08b') for x in str_to_conv)
# Функция для замены нескольких значений разом
def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str
# создаем словарь со значениями и строку, которую будет изменять
replace_values = {"0": "У", "1": "Г"}
# изменяем и печатаем строку
Conv = multiple_replace(bin_result, replace_values)
print(Conv)