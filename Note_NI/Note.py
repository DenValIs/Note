from Program import Note_pad

def Note():
    note_Pad = Note_pad()
    print("Выберите действие:\n\
    1) Новая заметка\n\
    2) Список заметок\n\
    3) Операции с заметками")
    select = input()
    if select == "1":
        note_Pad.add_note()
    if select == "2":
        note_Pad.list_note()
    if select == "3":
        note_Pad.select_note()