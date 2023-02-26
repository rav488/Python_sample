'''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
from tkinter import *
from datetime import *
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox

import sys

sys.path.append("../")
import zzplik as zz



a = []
global zajetepokoje
zajetepokoje = []
pokoje = [11,12,13,14,15,21,22,23,24,25,31,32,33,34,35]
baza3path = '../Baza_Hotelowa_v5/bazy_danych/dane3.txt'



def rezerwacja(ramka):

    for widgets in ramka.winfo_children():
        widgets.destroy()

    okno2 = ramka
    ramkadol = Frame(okno2, height =100)
    ramkadol.pack(side='bottom')


    checked = StringVar()

    dlug = len(a)

    cals = Calendar(okno2, selectmode = 'day',year = 2022, month = 4, day = 22, locale="PL")
    cals.pack()
    cale = Calendar(okno2, selectmode = 'day',year = 2022, month = 4, day = 22, locale="PL")
    cale.pack()


    #----generowanie zakresu dat 
    def date_range(start, end):
        start_date = datetime.strptime(start, '%d.%m.%Y').date()
        end_date = datetime.strptime(end, '%d.%m.%Y').date()
        delta = end_date - start_date 
        dates = [
            (start_date + timedelta(days=d)).strftime('%d.%m.%Y')
            for d in range(delta.days + 1)
        ]

        return dates
        
    #weryfikacja czy data rezerwacji jest juz zajęta
    def start_grad_date(start, end, i):
        
        a = zz.otpli(baza3path)
        zakres = date_range(start, end)
        podanystart = cals.get_date()
        podanykoniec = cale.get_date()
        if (podanystart in zakres) or (podanykoniec in zakres):
            nr_pok_test = a[i][0]

            costamzaj = Label(ramkadol, text = 'pokoj '+a[i][0]+' jest zajety')
            costamzaj.pack()
            zajetepokoje.append(nr_pok_test)




    #czyszczenie i wypisywanie w ramce
    def costam():
        zajetepokoje.clear()
        a = zz.otpli(baza3path)
        for widgets in ramkadol.winfo_children():
           widgets.destroy()
        global i
        i = 0
        while i < len(a):
            start = a[i][2]
            end = a[i][3]
            start_grad_date(start, end, i)
            i +=1

    def zapisac():

        per_list = zz.otpli(baza3path)
        nrpok = nr_pok.get()
        nazwiskog = nazwisko_.get()
        if nrpok in zajetepokoje:
            messagebox.showerror("showerror", "Już Zajęty!!!")
             
        else:
            datapoczatkowa = cals.get_date()
            datakoncowa = cale.get_date()
            tym = [nrpok, nazwiskog, datapoczatkowa, datakoncowa]
            per_list.append(tym)
            open(baza3path, "w").close()
            f = open(baza3path, "r+")
            for i in range(len(per_list)):
                for j in range(len(per_list[i])):
                    a = str(per_list[i][j])
                    f.write(a + ',')
                f.write(';')
            f.close()
        zz.okpokdod()

    nr_pok_lab = Label(okno2, text='Podaj nr pokoju')
    nr_pok_lab.pack()
    nr_pok = Entry(okno2, width=20)
    nr_pok.pack()


    nazwisko_lab = Label(okno2, text='Podaj Imie i Nazwisko Gościa')
    nazwisko_lab.pack()
    nazwisko_ = Entry(okno2, width=20)
    nazwisko_.pack()



    sprawdzbut = Button(okno2, text ='sprawdz', command = costam)
    sprawdzbut.pack()
    zapisbut = Button(okno2, text = 'rezerwoj', command = zapisac)
    zapisbut.pack()

    okno2.mainloop()

