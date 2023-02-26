from tkinter import *
import zzplik as zz

'''
    for widgets in ramkalewa.winfo_children():
                widgets.destroy()
'''
data4path = '../Baza_Hotelowa_v5/bazy_danych/dane4.txt'

def bilroom11():

                
    for i in range(len(lista)):
        if lista[i][0]==nrpok:
            lista11.append(lista[i][1])

    poduszka = str(lista11.count('poduszka'))        
    koc = str(lista11.count('koc'))
    piwo = str(lista11.count('piwo'))
    CocaCola = str(lista11.count('CocaCola'))
    ciastko = str(lista11.count('ciastko'))
    
    podsuma.set('\n\n'+poduszka+'\n'+koc+'\n'+piwo+'\n'+CocaCola+'\n'+ciastko)
    
    Label(root, text='Zamówiłeś:\n\nPoduszka:\nKoc:\nPiwo:\nCoca-Cola:\nCiastko:', justify = LEFT).pack(side=LEFT)
    Label(root, textvariable = podsuma, justify  = LEFT).pack(side=LEFT)

    poduszkaint = int(poduszka)
    if poduszkaint >= 0:
        poduszkacena = 5*poduszkaint
        poduszkacena = str(poduszkacena)
    kocint = int(koc)
    if kocint >= 0:
        koccena = 15*kocint
        koccena = str(koccena)
    piwoint = int(piwo)
    if piwoint >=0:
        piwocena = 5*piwoint
        piwocena = str(piwocena)
    colaint = int(CocaCola)
    if colaint >= 0:
        colacena = 1.2 * colaint
        colacena = str(round(colacena,2))
    ciastkoint = int(ciastko)
    if ciastkoint >= 0:
        ciastkocena = 1.5 * ciastkoint
        ciastkocena = str(ciastkocena)
    Label(root, text='\n\n   (5 zł)\n   (15 zł)\n   (5 zł)\n   (1.4 zł)\n   (1.5 zł)', justify  = LEFT).pack(side=RIGHT)
    lacznie.set('\n\n'+poduszkacena+' zł\n'+koccena+' zł\n'+piwocena+' zł\n'+colacena+' zł\n'+ciastkocena+' zł')    
    ceny = Label(root, textvariable = lacznie, justify = RIGHT)
    ceny.pack(side=RIGHT)
    


def spis(frame, nrpokinf):
    for widgets in frame.winfo_children():
        widgets.destroy()
    global root
    root = frame
    global nrpok    
    nrpok = StringVar()
    nrpok = nrpokinf
    global lista
    lista = zz.otpli(data4path)
    global lista11
    lista11 = []
    global podsuma
    podsuma = StringVar()
    global lacznie
    lacznie = StringVar()    
    global podsumacena
    podsumacena = StringVar()
    global koc
    koc = StringVar()
    global piwo
    piwo = StringVar()
    global CocaCola
    CocaCola = StringVar()
    global poduszka
    poduszka = StringVar()
    
    bilroom11()
    
    root.mainloop()
