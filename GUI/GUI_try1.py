# импорт либ
import PySimpleGUI as sg
import re
import string
import clipboard
# устанавливает стандартную тему библиотеки PySimpleGUI
sg.theme('DarkAmber') 
layout = [  
            [sg.Text('Введите текст для зашифровки'), sg.InputText()],
            [[sg.Text('Результат')],
                      [sg.Multiline(size=(60,15), key='-OUTPUT-', font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                    reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)],
            [sg.Button('ОК'), sg.Button('Выход')] ]]
replace_values = {"0": "У", "1": "Г"}
#Главное окно
window = sg.Window('Совиный язык', layout)
#Функция для замены символов
def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str
#Если ТРУЪ - выполняет всё что под табуляцией
while True:
    event, values = window.read()
    # Прекращение выполнения кода при нажатии кнопки 'Выход' или закрытии окна
    if event == sg.WIN_CLOSED or event == 'Выход': 
        break      
    # указываем что переменная text_crypt это сначало преобразованное по мат.формуле значение, а позже изменённое функцией multiple_replace
    text_crypt = multiple_replace((''.join(format(ord(x), '08b') for x in values[0])), replace_values)
    # выводит результат в окно с ключём -OUTPUT- (тоесть 'Результат')
    window['-OUTPUT-'].update(text_crypt)
    # копирует значеие text_crypt в буфер обмена с помощью библиотеки clipboard
    clipboard.copy(text_crypt)
# Закрытие окна
window.close()



