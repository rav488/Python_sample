from tkinter import *
import zzplik as zz
#szukana = 'pokój 11'
from tkinter import messagebox #messagebox.showerror("showinfo", "Już Zajęty!!!")

data4path = '../Baza_Hotelowa_v5/bazy_danych/dane4.txt'


def clearroom11():
    global kasowniki
    kasowniki = []
    for i in range(len(lista)):
        if szukana in lista[i][0]:
            kasowniki.append(i)
    kasowniki = kasowniki[::-1]
    print(kasowniki)

    for licznik2 in range(len(kasowniki)):
        pozycja = kasowniki[licznik2]
        del lista[pozycja]

    open(data4path, "w").close()
    frez = open(data4path, "r+")
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            a = str(lista[i][j])
            frez.write(a + ',')
        frez.write(';')
    frez.close()
    messagebox.showwarning("showwarning", "Usunięto rachunek")
    for widgets in root.winfo_children():
        widgets.destroy()
    print(lista)


def usuwanie(frame, nrpokinf):
    for widgets in frame.winfo_children():
        widgets.destroy()
        
    global root
    root = frame
    global a
    a = []
    global szukana
    szukana = nrpokinf
    global lista
    lista = zz.otpli(data4path)


    print(lista)

    pok11 = Button(root, text = 'POTWIERDŹ', command = clearroom11)
    pok11.pack()

    
    root.mainloop()
