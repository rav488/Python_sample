from tkinter import *
import sys

sys.path.append("../Baza_Hotelowa_v5/img")
import logoturtle as logo


sys.path.append("../Baza_Hotelowa_v5/guest_file")
import guest_list
sys.path.append("../Baza_Hotelowa_v5/guest_file")
import new_guest
sys.path.append("../Baza_Hotelowa_v5/guest_file")
import guest_delete

import zzplik as zz
sys.path.append("../Baza_Hotelowa_v5/reservation_file")
import rezerwacje
sys.path.append("../Baza_Hotelowa_v5/reservation_file")
import odbiorrezerwacji

sys.path.append("../Baza_Hotelowa_v5/rachunekpokoju")
import glowny as rach


#definicja komend Button

def start():
    for widgets in ramkalewa.winfo_children():
                widgets.destroy()
    #Label(ramkalewa, text = 'Witaj w naszym hotelu').pack()
    
    logo.logo(ramkalewa)
    
def ListGuest():
    guest_list.show_guest_list(ramkalewa)
    
def AddGuest():
    new_guest.dod_new_gos(ramkalewa)
    
def AddReservations():
    rezerwacje.rezerwacja(ramkalewa)
    
def DelGuest():
    guest_delete.usugoscokn(ramkalewa)
    
def DelReservations():
    odbiorrezerwacji.odb_rez(ramkalewa)
    
def BillHandling():
    rach.rachunek(ramkalewa)
 
# ustalanie onka
okno = Tk()
okno.geometry('1000x600')
global ramkalewa
ramkalewa = Frame(okno, width = 700, height = 700)
ramkalewa.pack(side='left')
ramkaprawa = Frame(okno, width =200, height = 700)
ramkaprawa.pack(side='right')

#----menu----
menubar = Menu(okno)
hotelmenu = Menu(menubar, tearoff = 0)
guestmenu = Menu(menubar, tearoff = 0)
reservationsmenu = Menu(menubar, tearoff = 0)
billsmenu = Menu(menubar, tearoff = 0)

hotelmenu.add_command(label = "Start", command = start)
hotelmenu.add_separator()
hotelmenu.add_command(label = "Lista Gosci", command = ListGuest)
hotelmenu.add_command(label = "Dodaj gościa", command = AddGuest)
hotelmenu.add_command(label = "Usuń gościa", command = DelGuest)
hotelmenu.add_separator()
hotelmenu.add_command(label = "REZERWACJE", command = AddReservations)
hotelmenu.add_command(label = "Odbierz / Usuń /nrezerwacje", command = DelReservations)
hotelmenu.add_separator()
hotelmenu.add_command(label = "Obsługa rachunków", command = BillHandling)
hotelmenu.add_separator()
hotelmenu.add_command(label = "Exit", command = okno.destroy)

guestmenu.add_command(label = "Lista Gosci", command = ListGuest)
guestmenu.add_command(label = "Dodaj gościa", command = AddGuest)
guestmenu.add_command(label = "Usuń gościa", command = DelGuest)

reservationsmenu.add_command(label = "REZERWACJE", command = AddReservations)
reservationsmenu.add_command(label = "Odbierz / Usuń /nrezerwacje", command = DelReservations)

billsmenu.add_command(label = "Obsługa rachunków", command = BillHandling)

menubar.add_cascade(label = "Hotel", menu = hotelmenu)
menubar.add_cascade(label = "Goście", menu = guestmenu)
menubar.add_cascade(label = "Rezerwacje", menu = reservationsmenu)
menubar.add_cascade(label = "Rachunki", menu = billsmenu)
#-----koniec menu-----

#ustalanie Button
start_button = Button(ramkaprawa, text = 'start', width = 23, command = start)
start_button.place(x=10,y=0)

list_guest = Button(ramkaprawa, text = 'Lista Gosci', width = 23, command = ListGuest)
list_guest.place(x=10,y=30)

add_guest = Button(ramkaprawa, text = 'Dodaj gościa', width = 23, command = AddGuest)
add_guest.place(x=10,y=60)

add_reservations = Button(ramkaprawa, text = 'REZERWACJE', width = 23, command = AddReservations)
add_reservations.place(x=10,y=90)

del_reservations = Button(ramkaprawa, text = 'Odbierz / Usuń /nrezerwacje', width = 23, command = DelReservations)
del_reservations.place(x=10,y=120)

bill_handling = Button(ramkaprawa, text = 'Obsługa rachunków', width = 23, command = BillHandling)
bill_handling.place(x=10,y=150)

del_guest = Button(ramkaprawa, text = 'Usuń gościa', width = 23, command = DelGuest)
del_guest.place(x=10,y=180)

exit_button = Button(ramkaprawa, text = 'Quit', compound=LEFT, width = 23, command = okno.destroy)
exit_button.place(x=10,y=210)




#---wywolanie menu
okno.config(menu = menubar)
#-----------
okno.mainloop()





