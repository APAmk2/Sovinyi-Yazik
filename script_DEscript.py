# импорт либ
import re
import string

# создаем словари заменяемых значений и переменные, на которые будет подменять
zero_key = 'У'
one_key = 'Г'
crypt_values = {"0": zero_key, "1": one_key}
encrypt_values = {zero_key: "0", one_key: "1"}
# Функции
## Функция для декодирования двоичного кода
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
## Функция для замены символов согласно словарю
### Какого хера это работает в обе стороны? Словарь replace_values не существует
def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str
# Зацикливаем скрипт вплоть до того, пока не будет выбран выход
while 1:
    print('1 - зашифровать, 2 - расшифровать, 3 - выход')
    choice = int(input('Введите что нужно сделать: '))
    # Зашифровка
    if choice == 1:
        print('Зашифровать')
        text = input('Введи текст: ')
        #print("Дебаг:строка для перевода: ",text)
        # указываем что переменная text_crypt это сначало преобразованное по мат.формуле значение, а позже изменённое функцией multiple_replace
        text_crypt = multiple_replace((''.join(format(ord(x), '08b') for x in text)), crypt_values)
        # Печатаем
        print(text_crypt)
    # Расшифровка
    if choice == 2:
        text = input('Введи шифр: ')
        # Указываем что значение text_encrypt это результат работы функции decode_binary_string с значением text_crypt переведённым в двоичный код функцией multiple_replace
        text_encrypt =decode_binary_string(multiple_replace(text, encrypt_values))
        # Печатаем 
        print (text_encrypt)
    # Выход
    if choice == 3:
        break