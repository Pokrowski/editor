import tkinter
from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import messagebox


class Text_editor():
    def __init__(self):
        self.file_name=NONE
    def new_file(self):
        self.file_name="Not name"
        text.delete('1.0',END)
    def save_file(self):
        data=text.get('1.0',END)
        output=open(self.file_name,'w',encoding="utf-8")
        output.write(data)
        output.close()
    def save_as_file(self):
        output=asksaveasfile(mode='w',defaultextension='txt') 
        data=text.get('1.0',END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title='Ошибка!',Message="Ошибка при сохранении файла.")
    def get_info(self):
        messagebox.showinfo("Справка","Информация о нашем приложении:")
    def open_file(self):
        inp = askopenfile(mode='r')
        if inp is None:
            return
        data = inp.read()
        text.delete('1.0',END)
        text.insert('1.0',data)
root = Tk()
root.title("Dead Note")
text = Text(root,width=97,font="Verdana 12",wrap=WORD)
scr = Scrollbar(root, orient=VERTICAL,command=text.yview)
scr.pack(side="right",fill="y")
text.configure(yscrollcommand=scr.set)
text.pack()


m = Menu(root)

root.config(menu=m)

editor=Text_editor()

fm = Menu(m)
m.add_cascade(label="File",menu=fm)
fm.add_command(label="New",command=editor.new_file)
fm.add_command(label="Open",command=editor.open_file)
fm.add_command(label="save as",command=editor.save_as_file) 
fm.add_command(label="Save",command=editor.save_file)

sm = Menu(m)
m.add_cascade(label="Help",menu=sm)
sm.add_command(label="Help")
sm.add_command(label="About",command=editor.get_info)

th=Menu(m)
m.add_cascade(label="Exit",command=exit)

root.mainloop()