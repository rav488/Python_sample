from tkinter import *
import tkinter.ttk as ttk

import rachunekpokoju_dodawanie as dod
import rachunekpokoju_odczyt as odcz
import rachunekpokoju_usuwanie as usu


'''
def usugoscokn(ramka):

    for widgets in ramka.winfo_children():
        widgets.destroy()

    okno4 = ramka
    '''
global nrpok



def combo():
    combobox = ttk.Combobox(ramkagora, textvariable = zmienna_combo)
    combobox.pack(side=LEFT)
    combobox['values'] = pokoje
    combobox.current(0) #pierwotny index
    combobox.bind("<<ComboboxSelected>>", ustalnrpok)

def ustalnrpok(b):
    global nrpok
    global nr_pok
    nrpok = StringVar()
    nr_pok = zmienna_combo.get()
    nrpok.set(nr_pok)

def dodaj_wyd():
    dod.dodawanie(ramkadol, nr_pok)
def odcz_pok():
    odcz.spis(ramkadol, nr_pok)
def usun_rach():
    usu.usuwanie(ramkadol, nr_pok)

def rachunek(frame):
    for widgets in frame.winfo_children():
        widgets.destroy()    
    root = frame
    global pokoje
    pokoje = ['11','12','13','14','15','21','22','23','24','25','31','32','33','34','35']
    global zmienna_combo
    zmienna_combo = StringVar()
    global nr_pok
    nr_pok = '11'

    global ramkagora
    global ramkasrodek
    global ramkadol
    ramkagora = Frame(root, height = 200)
    ramkagora.pack(side = 'top')
    ramkasrodek = Frame(ramkagora)
    ramkasrodek.pack(side = 'bottom')
    ramkadol = Frame(root, height = 300)
    ramkadol.pack(side = 'bottom')


    Label(ramkagora, text='Wybierz numer pokoju: ').pack(side=LEFT)
    Button(ramkasrodek, text='Dodaj artykuły', command = dodaj_wyd).pack(side='left')
    Button(ramkasrodek, text='Podsumowanie', command = odcz_pok).pack(side='left')
    Button(ramkasrodek, text='Skasuj rachunek', command = usun_rach).pack(side='left')
    combo()

    root.mainloop()
