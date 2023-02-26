from tkinter import *
#import tkinter as tk
import tkinter.ttk as ttk
import zzplik as zz
from tkinter import messagebox #messagebox.showerror("showinfo", "Już Zajęty!!!")

data4path = '../Baza_Hotelowa_v5/bazy_danych/dane4.txt'

    
def costam(b):
    global nrpok
    nrpok = str(cb_value.get())

def confirm():
    for string_var in all_string_vars:
        text = string_var.get()
        if text:
            b = text
            lista.append([nrpok,b])
            zapis()
    messagebox.showinfo("showinfo", "Dodano do rachunku")
    for widgets in root.winfo_children():
        widgets.destroy()

        
def zapis():
    open(data4path, "w").close()
    frez = open(data4path, "r+")
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            a = str(lista[i][j])
            frez.write(a + ',')
        frez.write(';')
    frez.close()

def dodawanie(frame, nrpokinf):
    for widgets in frame.winfo_children():
        widgets.destroy()
    global root
    root = frame
    global nrpok
    nrpok = StringVar()
    nrpok = nrpokinf
    #root = Tk()
    a = []
    items = ['poduszka', 'koc', 'piwo', 'CocaCola', 'ciastko'] 

    cb_value = StringVar()
    global lista
    lista = zz.otpli(data4path)

    listapokoj11 = []
    global all_string_vars
    all_string_vars = []







    for item in items:
        string_var = StringVar()
        cb = Checkbutton(root, text=item, variable=string_var, anchor='w', onvalue=item, offvalue='', width=15)
        cb.pack()
        all_string_vars.append(string_var)








    button = Button(root, text="Confirm", command=confirm)
    button.pack()

    root.mainloop()



