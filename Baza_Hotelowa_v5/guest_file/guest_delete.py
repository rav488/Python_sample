'''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''

from tkinter import *

import sys



sys.path.append("../")
import zzplik as zz

a = []

zm_nrpok = ''
zm_nazwisko = ''
zm_pesel = ''
baza2path = '../Baza_Hotelowa_v5/bazy_danych/dane2.txt'


#------------------------okno usuwanie goscia
def usugoscokn(frame):

    for widgets in frame.winfo_children():
        widgets.destroy()

    okno4 = frame
    
    # -----wczytanie bazy gosci
    per_list = zz.otpli(baza2path)



    def usuwaniegosci():
        a = pokusu.get()
        a = str(a)
        sprusu = []
        for row in per_list:
            if a in row:
                a = per_list.index(row)
                sprusu.append('tak')
            else:
                sprusu.append('nie')

        if 'tak' in sprusu:
            per_list.pop(a)
            zz.okpokdod()
        else:
            zz.okpokniem()

        f = open(baza2path, "w")
        for i in range(len(per_list)):
            for j in range(len(per_list[i])):
                a = str(per_list[i][j])
                f.write(a + ',')
            f.write(';')
        f.close()


    etyusu = Label(okno4, text='Podaj nr pokoju ktory zostal oprozniony')
    etyusu.pack()
    pokusu = Entry(okno4,width=20)
    pokusu.pack()

    global trash_img
    trash_img = PhotoImage(file="../Baza_Hotelowa_v5/img/trash_but.png")
    trash_img = trash_img.subsample(2)

    usubut = Button(okno4, text='USUN', image = trash_img, compound = LEFT ,width = 120, command=usuwaniegosci)
    usubut.pack()


    okno4.mainloop
