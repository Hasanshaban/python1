import tkinter as tk
from tkinter import *
import datetime



def write_dic_birthday():
    name = entry_name.get()
    birthday_date = entry_date.get()
    birthday[name] = birthday_date
    entry_name.delete(0, END)
    entry_date.delete(0, END)
def write_dic_file():
    date_object = str(datetime.date.today())
    print(date_object)
    file_birthday = open("Test.txt","a")
    file_birthday.write(date_object+str(birthday)+"\n")
    file_birthday.close()


global birthday
root=tk.Tk()
root.geometry("800x400")
root.title("birthday")
root.resizable(width=False, height=False)
label=tk.Label(root,text="نام")
label.place(x=600,y=100)
label=tk.Label(root,text="روز و ماه تولد")
label.place(x=600,y=150)
button=tk.Button(root,text="ثبت اطلاعات",command=write_dic_birthday)
button.place(x=600,y=200)

button1=tk.Button(root,text="ثبت کلی",command=write_dic_file)
button1.place(x=600,y=300)
entry_name=tk.Entry(root)
entry_name.place(x=400,y=100)
entry_date=tk.Entry(root)
entry_date.place(x=400,y=150)
birthday = {}


root.mainloop()

