from tkinter import *
import sys


sys.path.append("../")
import zzplik as zz

import new_guest
from functools import partial

baza2path = '../Baza_Hotelowa_v5/bazy_danych/dane2.txt'


def EntryBox(root_frame, w, h):
    boxframe = Frame(root_frame, width = w+2, height= h+2, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=0)

    boxframe.pack()
    return boxframe

def ShowRoom(f,i):
        Label(labels[f], text=lista[i][0]).pack()
        Label(labels[f], text=lista[i][1]).pack()
        Label(labels[f], text=lista[i][2]).pack()
        Label(labels[f], text=lista[i][3]).pack()
def ShowRoomFree(f,i):
        Label(labels[f], text='Wolne').pack()


def nowygosc(r):

    if r == 0:
        new_guest.dod_new_gos(root, '11')
    if r == 3:
        new_guest.dod_new_gos(root, '12')
    if r == 6:
        new_guest.dod_new_gos(root, '13')                 
    if r == 9:
        new_guest.dod_new_gos(root, '14')                 
    if r == 12:
        new_guest.dod_new_gos(root, '15')

    if r == 1:
        new_guest.dod_new_gos(root, '21')
    if r == 4:
        new_guest.dod_new_gos(root, '22')
    if r == 7:
        new_guest.dod_new_gos(root, '23')                 
    if r == 10:
        new_guest.dod_new_gos(root, '24')                 
    if r == 13:
        new_guest.dod_new_gos(root, '25')        

    if r == 2:
        new_guest.dod_new_gos(root, '31')
        
    if r == 5:
        new_guest.dod_new_gos(root, '32')
    if r == 8:
        new_guest.dod_new_gos(root, '33')                 
    if r == 11:
        new_guest.dod_new_gos(root, '34')                 
    if r == 14:
        new_guest.dod_new_gos(root, '35')
    


    
                
def show_guest_list(frame):

    global root
    for widgets in frame.winfo_children():
        widgets.destroy()

    root = frame
    root.configure(height = 500)

    global costam
    global labels
    global lista
    costam = []
    labels = []
    lista = zz.otpli(baza2path)

    

    for i in range(5):
        for j in range(3):
            box = EntryBox(root, 20, 20)
            box.place(x = 50 + i*100, y = 30 + j*80 , width = 100, height = 80)
            labels.append(box)

    for i in range(len(lista)):
        if '11' in lista[i]:
            ShowRoom(0,i)
        if '21' in lista[i]:
            ShowRoom(1,i)
        if '31' in lista[i]:
            ShowRoom(2,i)        
        if '12' in lista[i]:
            ShowRoom(3,i)
        if '22' in lista[i]:
            ShowRoom(4,i)
        if '32' in lista[i]:
            ShowRoom(5,i)        
        if '13' in lista[i]:
            ShowRoom(6,i)
        if '23' in lista[i]:
            ShowRoom(7,i)
        if '33' in lista[i]:
            ShowRoom(8,i)        
        if '14' in lista[i]:
            ShowRoom(9,i)
        if '24' in lista[i]:
            ShowRoom(10,i)
        if '34' in lista[i]:
            ShowRoom(11,i)        
        if '15' in lista[i]:
            ShowRoom(12,i)
        if '25' in lista[i]:
            ShowRoom(13,i)
        if '35' in lista[i]:
            ShowRoom(14,i)        
            

    for i in range(len(labels)):
        global room_variable

        room_info = labels[i].winfo_children()
        if room_info == costam:
            Label(labels[i],text='Wolne').pack()
            room_variable = labels[i]
            action_with_arg = partial(nowygosc, i)
             
            reserv_button = Button(labels[i],text='Rezerwoj', command = action_with_arg)
            reserv_button.pack()
    
    root.mainloop()
