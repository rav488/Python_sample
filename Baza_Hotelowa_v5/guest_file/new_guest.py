'''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
from tkinter import *
import sys



sys.path.append("../")
import zzplik as zz

from datetime import *

a = []

roomnum = ''
zm_sername = ''
zm_pesel = ''
baza2path = "../Baza_Hotelowa_v5/bazy_danych/dane2.txt"
baza3path = "../Baza_Hotelowa_v5/bazy_danych/dane3.txt"
#-------------------------- okno nowy gosc
def dod_new_gos(frame, nrpok_var='00'):
    for widgets in frame.winfo_children():
        widgets.destroy()
    okno3 = frame
    zmienna = StringVar()
    zmienna.set(nrpok_var)

    # -----wczytanie bazy gosci
    per_list = zz.otpli(baza2path)
    rez_list = zz.otpli(baza3path)

    # -----tu sie konczy

    weryf = []

    nrpokop = Label(okno3, text='Nr Pokoju:')
    nrpokop.pack()
    nrpok = Entry(okno3, textvariable= zmienna, width=20)
    nrpok.pack()
    nazwiskoop = Label(okno3, text = 'Nazwisko :')
    nazwiskoop.pack()
    nazwisko = Entry(okno3, width=20)
    nazwisko.pack()
    nrpeselop = Label(okno3, text = 'Pesel :')
    nrpeselop.pack()
    nrpesel = Entry(okno3, width=20)
    nrpesel.pack()
    declaration_day_label = Label(okno3, text = 'Do kiedy wynajem:\n(dd.mm.rrrr)')
    declaration_day_label.pack()
    declaration_day = Entry(okno3, width = 20)
    declaration_day.pack()

    def zapisac():

        weryf.clear()

        roomnum = nrpok.get()
        zm_sername = nazwisko.get()
        zm_pesel = nrpesel.get()
        data_rej = date.today().strftime('%d.%m.%Y')
        data_end = declaration_day.get()
#---------------------------------------------sprawdz czy nie zajete
        def weryfikacja():

            for i in range(len(per_list)):
                if roomnum in per_list[i]:
                    weryf.append('jest')
                else:
                    weryf.append('nie')

        weryfikacja()
        if 'jest' in weryf:
            zz.okpokzaj()
        else:
            per_list.append([roomnum, zm_sername, zm_pesel, data_rej,data_end])
#----------zapisanie listy z nowym pokojem
            open(baza2path, "w").close()
            f = open(baza2path, "r+")
            for i in range(len(per_list)):
                for j in range(len(per_list[i])):
                    a = str(per_list[i][j])
                    f.write(a + ',')
                f.write(';')
            f.close()
#----------tu sie konczy zapis
#----------zapis danych do pliku rezerwacji

            
            rez_list.append([roomnum, zm_sername, data_rej, data_end])
            open(baza3path, "w").close()
            frez = open(baza3path, "r+")
            for i in range(len(rez_list)):
                for j in range(len(rez_list[i])):
                    a = str(rez_list[i][j])
                    frez.write(a + ',')
                frez.write(';')
            frez.close()



            
            zz.okpokdod()


            
    img_klucz = PhotoImage(file="../Baza_Hotelowa_v5/img/key_but.png")
    img_klucz = img_klucz.subsample(2)
    zapiszgos = Button(okno3, text='zapisz', image = img_klucz, compound=LEFT, width = 180, command=zapisac)
    zapiszgos.pack()




    
    okno3.mainloop()

