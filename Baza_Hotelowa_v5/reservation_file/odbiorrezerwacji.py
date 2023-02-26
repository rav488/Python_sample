from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msb
from datetime import *

import sys
sys.path.append("../")
import zzplik as zz

baza2path = '../Baza_Hotelowa_v5/bazy_danych/dane2.txt'
baza3path = '../Baza_Hotelowa_v5/bazy_danych/dane3.txt'


#888888tu wklejone

weryf = []



def odb_rez(ramka):
    for widgets in ramka.winfo_children():
        widgets.destroy()
    window = ramka

    ramkagora = Frame(window, height =100)
    ramkagora.pack(side='top')


    # wypisywanie zmiennych do pol entry    
    def chech(b):


        a = str(cb_value.get())
        #print(a)
        for i in range(len(listawzor)):
            if a in listawzor[i]:
                global balk
                balk = StringVar()
                global balk2
                balk2 = StringVar()
                global balk3
                balk3 = StringVar()
                global balk4
                balk4 = StringVar()
                balk = str(listawzor[i][0])
                balk2 =str(listawzor[i][1])
                balk3 = str(listawzor[i][3])
                balk4 = str(listawzor[i][2])
        wybor1.set(balk)
        wybor2.set(balk2)
        wybor3.set(balk3)
        wybor4.set(balk4)



    # odbior rezerwacji i zapis w bazie klientow

    def zapisac():

        weryf.clear()

        roomnum = nr_pok_r.get()
        zm_sername = imie_r.get()
        zm_pesel = nr_pesel_r.get()
        data_rej = date.today().strftime('%d.%m.%Y')
        data_end = data_r.get()
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




                
        zz.okpokdod()








        
    # usuwanie rezerwacji z bazy danych
    def usuwaniegosci():
        a = imie_r.get()
        a = str(a)
        sprusu = []
        for row in listawzor:
            if a in row:
                a = listawzor.index(row)
                sprusu.append('tak')
            else:
                sprusu.append('nie')

        if 'tak' in sprusu:
            listawzor.pop(a)
            zz.okpokdod()
        else:
            zz.okpokniem()

        f = open(baza3path, "w")
        for i in range(len(listawzor)):
            for j in range(len(listawzor[i])):
                a = str(listawzor[i][j])
                f.write(a + ',')
            f.write(';')
        #print(per_list)
        f.close()
        #odb_rez()
        odswiez()


    #tworzenie comboboxa
    def combolista():
        #cb_value = StringVar() # zmienna typu StringVar, która zostanie podpięta pod kontrolkę Combobox



        combobox = ttk.Combobox(ramkagora, textvariable = cb_value) # tworzenie kontrolki Combobox
        combobox.pack(pady=10)
        #combobox.place(x = 50, y = 10) # umieszczenie kontrolki na oknie głównym
        combobox['values'] = lista # ustawienie elementów zawartych na liście rozwijanej
        combobox.current(0) # ustawienie domyślnego indeksu zaznaczenia
        combobox.bind("<<ComboboxSelected>>", chech)
        
    def odswiez():
        global lista
        listawzor = zz.otpli(baza3path)
        lista = []
        for i in range(len(listawzor)):
            lista.append(listawzor[i][1])
        for widgets in ramkagora.winfo_children():
           widgets.destroy()
        return combolista()
    # ----------------------------------------------definiowanie okna    
    #window = Tk()
    #window.geometry('300x400')

    #deklarowanie zmiennych
#888888888tu wyciete
    wybor1 = StringVar()
    wybor1.set('nr pokoju')
    wybor2 = StringVar()
    wybor2.set('Imie i Nazwisko')
    wybor3 = StringVar()
    wybor3.set('Do kiedy pokoj')
    wybor4 = StringVar()
    wybor4.set('Od kiedy pokoj')
    wybor5 = StringVar()
    wybor5.set('Nr Pesel(do rejestracji)')
    cb_value = StringVar()
    per_list = zz.otpli(baza2path)

    #czesc wlasciwa
    listawzor = zz.otpli(baza3path)

    odswiez()


    #odbierz.place(x=0, y=200)


    nr_pok_r = Entry(window, textvariable=wybor1)
    nr_pok_r.pack(padx = 40, pady=0)#place(x = 50, y = 50)
    imie_r = Entry(window, textvariable=wybor2)
    imie_r.pack(pady=0)#place(x = 50, y = 80)
    data_od = Entry(window, textvariable=wybor4)
    data_od.pack()#place(x = 50, y = 110)
    data_r = Entry(window, textvariable=wybor3)
    data_r.pack()#place(x = 50, y = 140)
    nr_pesel_r = Entry(window, textvariable=wybor5)
    nr_pesel_r.pack()#place(x = 50, y = 170)

    usun = Button(window, text='Usuń rezerwacje', command = usuwaniegosci)
    usun.pack()
    #usun.place(x=120, y=200)

    odbierz = Button(window, text='Odbierz rezerwacje', command = zapisac)
    odbierz.pack()

    window.mainloop()
