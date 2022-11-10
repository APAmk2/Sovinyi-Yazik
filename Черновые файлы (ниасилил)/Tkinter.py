from tkinter import *
import re
import string

zero_def = ''
one_def = ''
replace_values = {"0": zero_def, "1": one_def}


root = Tk()
root.title("NOT FOUND")
root.geometry('960x360')
text = Text(width=80, height=15, wrap=WORD)
Res = Text(width=60, height=15)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=RIGHT, fill=Y)
 
Res.config(yscrollcommand=scroll.set)


text.pack()
root.mainloop()