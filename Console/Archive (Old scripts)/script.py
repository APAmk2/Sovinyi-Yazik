# импорт либ
import re
import string

# создаем словарь заменяемых значений и переменные, на которые будет подменять

zero_key = 'У'
one_key = 'Г'
replace_values = {"0": zero_key, "1": one_key}

# Создаём переменную и записываем в неё текст
text = input('Введи текст: ')
# Выводим строку которую переведём (Дебаг)
print("Дебаг:строка для перевода: ",text) 

# Функция для замены нескольких значений разом
def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str

# указываем что переменная text_crypt это сначало преобразованное по мат.формуле значение, а позже изменённое функцией multiple_replace
text_crypt = multiple_replace((''.join(format(ord(x), '08b') for x in text)), replace_values)
# Выводим итоговое значение
print(text_crypt)