import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import askyesno
from git import Repo
root = Tk()
root.title("Упаковщик и редактор лицензии")
root.geometry("750x750")
pathes_of_files=[]
combobox = ttk.Combobox(values=pathes_of_files)
combobox.pack()
label = Label()
label.pack()
licension_editor = Text()
licension_editor.pack()

def open_file():
    openpath = filedialog.askopenfilename()
    if openpath != "":
        with open(openpath, "r") as file:
            text =file.read()
            licension_editor.delete("1.0", END)
            licension_editor.insert("1.0", text) 
def save_file():
    savepath = filedialog.asksaveasfilename()
    if savepath != "":
        text = licension_editor.get("1.0", END)
        with open(savepath, "w") as file:
            file.write(text)

def add_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        pathes_of_files.append(filepath)
        print(pathes_of_files)
        combobox.configure(values=pathes_of_files)
def delete_file():
    pathes_of_files.remove(combobox.get())
    combobox.configure(values=pathes_of_files)
    combobox.delete(0,'end')
    label.configure(text=f'Вы удалили файл. Всего {str(len(pathes_of_files))} файлов')
open_button = ttk.Button(text="Открыть лицензию", command=open_file)
open_button.pack()
 
save_button = ttk.Button(text="Сохранить лицензию", command=save_file)
save_button.pack()
add_button = ttk.Button(text="Добавить файл", command=add_file)
add_button.pack()
delete_button = ttk.Button(text="Удалить файл", command=delete_file)
delete_button.pack()

def selected(event):
    selection = combobox.get()
    label["text"] = f"Вы выбрали: {selection}. Всего {str(len(pathes_of_files))} файлов"
combobox.bind("<<ComboboxSelected>>", selected)
label1 = Label(text = 'Введите ссылку для загрузки в гитхаб')
label1.pack()
entry = Entry()
entry.pack()
def create_package():
    repo_dir = entry.get()
    repo = Repo(repo_dir)
    file_list = pathes_of_files
    commit_message = 'Files are added'
    repo.index.add(file_list)
    repo.index.commit(commit_message)
    origin = repo.remote('origin')
    origin.push()
def no_creating():
    label.configure(text='')
    licension_editor.delete(0, 'end')
    combobox.delete(0,'end')
    combobox.configure(values=[])
    result = askyesno(title="Выход", message="Закрыть установщик?")
    if result: root.quit()
create_button=Button(text="Создать установщик", command=create_package)
create_button.pack()
cansel_button=Button(text="Отмена", command=no_creating)
cansel_button.pack()
root.mainloop()
