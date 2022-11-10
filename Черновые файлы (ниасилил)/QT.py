from tkinter import *
import re
import string

window = Tk()
replace_values = {"0": "У", "1": "Г"}

def clicked():
    Res = multiple_replace(bin, replace_values)
    lbl.configure(text=Res)


window.title("Совиный Язык")
window.geometry('640x240')
txt = Entry(window,width=10)  
txt.grid(column=1, row=3) 
btn = Button(window, text="Зашифровать", command=clicked)  
btn.grid(column=2, row=3)  
lbl = Label()
lbl.grid(column=0, row=0)

conv= "Шифр {}".format(txt.get())
bin = ''.join(format(ord(x), '08b') for x in conv)

def multiple_replace(target_str, replace_values):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i, j in replace_values.items():
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, j)
    return target_str




window.mainloop()
