from tkinter import *
import zzplik as zz

'''
    for widgets in ramkalewa.winfo_children():
                widgets.destroy()
'''


def bilroom11():
    for widgets in ramkadol.winfo_children():
                widgets.destroy()
                
    for i in range(len(lista)):
        if lista[i][0]=='pokój 11':
            lista11.append(lista[i][1])
    #print(lista11)
    koc = str(lista11.count('koc'))
    piwo = str(lista11.count('piwo'))
    CocaCola = str(lista11.count('CocaCola'))
    poduszka = str(lista11.count('poduszka'))
    podsuma.set('Zamówiłes :\n\nKoc : ' + koc + '\nPiwo : ' + piwo + '\nCocaCola : ' + CocaCola + '\npoduszka : ' + poduszka)
    #podsuma.set('blabla')
    Label(ramkadol, textvariable = podsuma, justify  = LEFT).pack(pady=50)


root = Tk()
root.geometry('300x300')
lista = zz.otpli('dane4.txt')
lista11 = []
podsuma = StringVar()
koc = StringVar()
piwo = StringVar()
CocaCola = StringVar()
poduszka = StringVar()

ramkagora = Frame(root, height = 100)
ramkagora.pack(side='top')
ramkadol = Frame(root)
ramkadol.pack(side='bottom')

pok11 = Button(ramkagora, text = 'pokoj 11', command = bilroom11)
pok11.pack()
    
root.mainloop()
