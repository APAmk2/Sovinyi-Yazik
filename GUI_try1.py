import PySimpleGUI as sg
import re
import string
import clipboard

sg.theme('DarkAmber')   # Add a touch of color
# All the stuff inside your window.
layout = [  
            [sg.Text('Введите текст для зашифровки'), sg.InputText()],
            [[sg.Text('Результат')],
                      [sg.Multiline(size=(60,15), key='-OUTPUT-', font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                                    reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)],
            [sg.Button('ОК'), sg.Button('Выход')] ]]
replace_values = {"0": "У", "1": "Г"}
# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Выход': # if user closes window or clicks cancel
        break      
    bin_result = ''.join(format(ord(x), '08b') for x in values[0])
    Res = multiple_replace(bin_result, replace_values)
    window['-OUTPUT-'].update(bin_result)
    clipboard.copy(bin_result)
window.close()



