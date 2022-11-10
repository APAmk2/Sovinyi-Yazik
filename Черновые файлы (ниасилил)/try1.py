import tkinter as tk
from tkinter import messagebox as msg
from tkinter.ttk import Notebook

import re
import string

replace_values = {"0": "У", "1": "Г"}

conv=(self.input_entry.get)
bin_result = ''.join(format(ord(x), '08b') for x in conv)
Res = multiple_replace(bin_result, replace_values)

class TranslateBook(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Совиный язык")
        self.geometry("500x300")

        self.notebook = Notebook(self)

        input_tab = tk.Frame(self.notebook)
        output_tab = tk.Frame(self.notebook)

        self.translate_button = tk.Button(input_tab, text="Зашифровать", command=self.translate)
        self.translate_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.input_entry = tk.Text(input_tab, bg="white", fg="black")
        self.input_entry.pack(side=tk.TOP, expand=1)

        self.output_copy_button = tk.Button(output_tab, text="Скопировать в буфер", command=self.copy_to_clipboard)
        self.output_copy_button.pack(side=tk.BOTTOM, fill=tk.X)

        self.output_translation = tk.StringVar(output_tab)
        self.output_translation.set("")

        self.output_label = tk.Label(output_tab, textvar=self.output_translation, bg="lightgrey", fg="black")
        self.output_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        self.notebook.add(input_tab, text="Незашифрованный")
        self.notebook.add(output_tab, text="Зашифрованный")

        self.notebook.pack(fill=tk.BOTH, expand=1)

    

    def multiple_replace(target_str, replace_values):
        # получаем заменяемое: подставляемое из словаря в цикле
        for i, j in replace_values.items():
            # меняем все target_str на подставляемое
            target_str = target_str.replace(i, j)
        return target_str


    def translate(self, text=None):
        if not text:
            self.output_translation.set(Res)
            msg.showinfo("Зашифровано", "Текст успешно зашифрован")

    def copy_to_clipboard(self, text=None):
        if not text:
            text = self.output_translation.get()

        self.clipboard_clear()
        self.clipboard_append(text)
        msg.showinfo("Copied Successfully", "Text copied to clipboard")


if __name__ == "__main__":
    translatebook = TranslateBook()
    translatebook.mainloop()
