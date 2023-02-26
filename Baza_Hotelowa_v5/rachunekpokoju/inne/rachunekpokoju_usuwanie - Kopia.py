from tkinter import *
import zzplik as zz
szukana = 'pokój 11'
lista = zz.otpli('dane4.txt')
a = []

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

    open("dane4.txt", "w").close()
    frez = open("dane4.txt", "r+")
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            a = str(lista[i][j])
            frez.write(a + ',')
        frez.write(';')
    frez.close()
    print(lista)
    
root = Tk()
root.geometry('300x300')
#lista = [[1,'a'],[1,'a'],[1,'a'],[2,'b'],[2,'b'],[2,'b'],[1,'a'],[2,'b']]



print(lista)

pok11 = Button(root, text = 'pokoj 11 - wyczysc zamownia', command = clearroom11)
pok11.pack()

    
root.mainloop()
