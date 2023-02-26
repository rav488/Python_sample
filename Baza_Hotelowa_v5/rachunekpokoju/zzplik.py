'''
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
from tkinter import *


def otpli(filepath):
    per_list = []
    f = open(filepath, "r+")
    test = f.read()
    per_list = test.split(";")
    per_list.pop()
    for i in range(len(per_list)):
        per_list[i] = per_list[i].split(',')
        per_list[i].pop()    
    
    f.close()
    return per_list
def okpokzaj():      # ---- okienko zajete
    zaj = Toplevel()
    etyk = Label(zaj, text='zajete')
    etyk.pack()
    ok = Button(zaj, text='ok', width=30, command=zaj.destroy)
    ok.pack()
    zaj.mainloop

def okpokdod():      # ---- okienko operacja pomyslna
    doda = Toplevel()
    etyk = Label(doda, text='Operacja wykonana pomyślnie')
    etyk.pack()
    ok = Button(doda, text='ok', command=doda.destroy)
    ok.pack()
    doda.mainloop

def okpokniem():      # ---- okienko był wolny
    niema = Toplevel()
    etyk = Label(niema, text='Ten pokoj był już wolny')
    etyk.pack()
    ok = Button(niema, text='ok', command=niema.destroy)
    ok.pack()
    niema.mainloop
