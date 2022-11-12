# Импортируем либы
import PySimpleGUI as sg
import re
import string
import clipboard
# устанавливает стандартную тему библиотеки PySimpleGUI
sg.theme('DarkAmber') 
layout = [
            [sg.Text('Введите текст для расшифровки'), sg.InputText()],
            [[sg.Text('Результат')],
                      [sg.Multiline(size=(60,15), key='-OUTPUT-', font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                    reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)],
            [sg.Button('ОК'), sg.Button('Выход')] ]]
replace_values = {"У": "0", "Г": "1"}
#Главное окно
window = sg.Window('Совиный язык', layout)
#Функция для замены символов
def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str
# функция для декодирования двоичного кода
def decode_binary_string(s):
    return ''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8))
#Если ТРУЪ - выполняет всё что под табуляцией
while True:
    event, values = window.read()
    # Прекращение выполнения кода при нажатии кнопки или закрытии окна
    if event == sg.WIN_CLOSED or event == 'Выход': 
        break      
    # указываем что переменная text_encrypt это преобразованный в двоичный код шифр, а позже сконвертированный в текст
    text_encrypt = decode_binary_string (multiple_replace(values[0], replace_values))
    # выводит результат в окно с ключём -OUTPUT- (тоесть 'Результат')
    window['-OUTPUT-'].update(text_encrypt)
    # копирует значеие text_encrypt в буфер обмена с помощью библиотеки clipboard
    clipboard.copy(text_encrypt)
# Закрытие окна
window.close()

