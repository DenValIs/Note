from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename 
 
file_name = NONE

def new_file():
    global file_name
    file_name = "NoName"
    txt_edit.delete("1.0", END)
 
def open_file():
    filepath = askopenfilename(
        filetypes=[("Текстовые файлы", "*.json"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(END, text)
    window.title(f"Заметки - {filepath}")
 
def save_file():
    filepath = asksaveasfilename(
        defaultextension=".json",
        filetypes=[("Текстовые файлы", "*.json"), ("Все файлы", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = txt_edit.get("1.0", END)
        output_file.write(text)
    window.title(f"Заметки - {filepath}")
 
 
window = Tk()
window.title("Заметки")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
 
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_new = Button(fr_buttons, text="Новый файл", command=new_file)
btn_open = Button(fr_buttons, text="Открыть файл", command=open_file)
btn_save = Button(fr_buttons, text="Сохранить как", command=save_file)
 
btn_new.grid(row=0, column=0, sticky="ew", padx=8,)
btn_open.grid(row=1, column=0, sticky="ew", padx=8, pady=15)
btn_save.grid(row=2, column=0, sticky="ew", padx=8)
 
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
 
window.mainloop()
