import tkinter as tk
window = tk.Tk()

x=50
y=50

button_dic = {'0':[50,200, 12], 
'1':[50,50,5], '2':[100,50,5], '3':[150,50,5], 
'4':[50,100,5], '5':[100,100,5], '6':[150,100,5], 
'7':[50,150,5], '8':[100,150,5], '9':[150,150,5],
'.':[150,200,5]}

number1 = ""
wynik = 0
var = tk.StringVar()
operacja = None
press = False


def nbr_write(par):
    global number1, press, wynik, operacja
    if press:
        if par =='.':
            number1 = '0.'
        else:
            number1 = par
        wynik = 0
        operacja = None
        press = False
    else:
        if par =='.':
            if number1 =='':
                number1 = '0.'
            else:
                number1 += '.'
        else:
            number1 += par
    var.set(number1)


def suma():
    global wynik, number1, press, operacja
    if press:
        number1 = str(wynik)
        wynik = 0
        press = False
    operacja = 'sum'
       
    if number1 =='':
        number1 ='0'
    if wynik == 0:
        wynik = float(number1)
    else:
        wynik = wynik + float(number1)
    number1 =''
    var.set(wynik)



def odejmowanie():
    global wynik, number1, operacja, press
    operacja = 'ode'
    if press:
        number1 = str(wynik)
        wynik = 0
        press = False
    if number1 =='':
        number1 ='0'
    if wynik == 0:
        wynik = float(number1)
    else:
        wynik = wynik - float(number1)
    number1 =''
    var.set(wynik)


def mnozenie():
    global wynik, number1, operacja, press
    operacja = 'mno'
    if press:
        number1 = str(wynik)
        wynik = 0
        press = False
    if number1 =='':
        number1 ='0'
        temp = 1
    else:
        temp = number1
    if wynik == 0:
        wynik = float(temp)
    else:
        wynik = wynik * float(temp)
    number1 =''
    var.set(wynik)

def dzielenie():
    global wynik, number1, operacja
    operacja = 'dzie'
    global press
    if press:
        number1 = str(wynik)
        wynik = 0
        press = False
    if number1 =='':
        number1 ='0'
        temp = 1
    else:
        temp = number1        
    if wynik == 0:
        wynik = float(temp)
    else:
        wynik = wynik / float(temp)
    number1 =''
    var.set(wynik)
    

def enter():
    global wynik, number1, press

    if number1 =='':
        number1 = '0'
    if operacja == 'sum':
        wynik += float(number1)
    if operacja =='ode':
        wynik -= float(number1)    
    if operacja == 'mno':
        wynik *= float(number1)
    if operacja =='dzie':
        wynik /= float(number1)          
    else:
        pass
    var.set(wynik)
    press = True

def clear():
    global number1, wynik, operacja, press
    number1 = ""
    wynik = 0
    operacja = None
    press = False
    var.set(wynik)

def clearnum():
    global number1
    number1 =''
    var.set(number1)

window.geometry('350x300')
window.title('Kalkulator')

numscr = tk.Entry(window, textvariable=var, width = 15, font=('Arial 22'))
numscr.place(x = x, y = y-40)

for nbrbut in button_dic:

    but_name = tk.Button(window, text=nbrbut, width=button_dic[nbrbut][2], height=2, command=lambda e=nbrbut: nbr_write(e))
    but_name.place(x= button_dic[nbrbut][0], y= button_dic[nbrbut][1])

buttonplus = tk.Button(window, text = '+', width=5, height=2, command=suma)
buttonplus.place (x=x+150, y = y)
buttonminus = tk.Button(window, text = '-', width=5, height=2, command=odejmowanie)
buttonminus.place (x=x+150, y = y+50)
buttonrazy = tk.Button(window, text = '*', width=5, height=2, command=mnozenie)
buttonrazy.place (x=x+150, y = y+100)
buttondziel = tk.Button(window, text = '/', width=5, height=2, command=dzielenie)
buttondziel.place (x=x+150, y = y+150)


buttonc = tk.Button(window, text = 'C', width=5, height=2, command=clear)
buttonc.place(x=x+200, y=y)
buttonce = tk.Button(window, text = 'CE', width=5, height=2, command=clearnum)
buttonce.place(x=x+200, y=y+50)
buttonE = tk.Button(window, text = '=', width=5, height=5, command=enter)
buttonE.place(x = x+200,y = y+100)

window.mainloop()
