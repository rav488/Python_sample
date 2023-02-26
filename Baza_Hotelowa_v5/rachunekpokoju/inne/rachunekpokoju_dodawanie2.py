from tkinter import *
#import tkinter as tk
import tkinter.ttk as ttk
import zzplik as zz
from tkinter import messagebox #messagebox.showerror("showinfo", "Już Zajęty!!!")

def combo():
    combobox = ttk.Combobox(root, text='wybierz pokoj', textvariable = cb_value) # tworzenie kontrolki Combobox
    combobox.pack()  #(x = 50, y = 10) # umieszczenie kontrolki na oknie głównym
    combobox['values'] = rooms # ustawienie elementów zawartych na liście rozwijanej
    combobox.current(0) # ustawienie domyślnego indeksu zaznaczenia
    combobox.bind("<<ComboboxSelected>>", costam)


    
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
'''
def podsuma():
    for i in range(len(zamowienie)):
        if zamowienie[i][0]=='pokój 11':
            listapokoj11.append(zamowienie[i][1])
'''            

        
def zapis():
    open("dane4.txt", "w").close()
    frez = open("dane4.txt", "r+")
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            a = str(lista[i][j])
            frez.write(a + ',')
        frez.write(';')
    frez.close()





root = Tk()
a = []
rooms = ['pokój 11','pokój 12','pokój 13','pokój 14']
items = ['poduszka', 'koc', 'piwo', 'CocaCola', 'ciastko'] 
#zamowienie = []
cb_value = StringVar()
lista = zz.otpli('dane4.txt')
nrpok = 'pokój 11'


listapokoj11 = []
all_string_vars = []


combo()




for item in items:
    string_var = StringVar()
    cb = Checkbutton(root, text=item, variable=string_var, anchor='w', onvalue=item, offvalue='', width=15)
    cb.pack()
    all_string_vars.append(string_var)








button = Button(root, text="Confirm", command=confirm)
button.pack()
#rachunek = Button(root, text='Rachunek', command = podsuma)
#rachunek.pack()
root.mainloop()



