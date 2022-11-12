# импорт либ
import re
import string

# создаем словарь со значениями и строку, которую будет изменять
zero_key = 'У'
one_key = 'Г'
replace_values = {zero_key: "0", one_key: "1"}

# Записываем в переменную зашифрованный текст
text_crypt = input('Введите шифр: ')
# Функция для замены нескольких значений
def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str

# функция для декодирования двоичного кода
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))

# Указываем что значение text_encrypt это результат работы функции decode_binary_string с значением text_crypt переведённым в двоичный код функцией multiple_replace
text_encrypt =decode_binary_string(multiple_replace(text_crypt, replace_values))

# Печатает готовый результат
print (text_encrypt)





