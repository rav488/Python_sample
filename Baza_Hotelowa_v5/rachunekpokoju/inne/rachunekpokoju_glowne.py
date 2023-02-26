from tkinter import *
#import tkinter as tk
import tkinter.ttk as ttk
import zzplik as zz
from tkinter import messagebox #messagebox.showerror("showinfo", "Już Zajęty!!!")
import rachunekpokoju_dodawanie as dodawanie



def combo():
    combobox = ttk.Combobox(root, text='wybierz pokoj', textvariable = cb_value) # tworzenie kontrolki Combobox
    combobox.pack()  #(x = 50, y = 10) # umieszczenie kontrolki na oknie głównym
    combobox['values'] = rooms # ustawienie elementów zawartych na liście rozwijanej
    combobox.current(0) # ustawienie domyślnego indeksu zaznaczenia
    combobox.bind("<<ComboboxSelected>>", costam)


    
def costam(b):
    global nrpok
    nrpok = str(cb_value.get())




root = Tk()

rooms = ['pokój 11','pokój 12','pokój 13','pokój 14']
cb_value = StringVar()
nrpok = 'pokój 11'

combo()


root.mainloop()



