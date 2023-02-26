from tkinter import *
from turtle import *

def stworz(okno):
    global ramka
    ramka = Canvas(okno)
    #ramka = okno
    ramka.config(width = 600, height = 500)
    ramka.pack(side=LEFT)
def logo(okno):
    #okno = Tk()    #definicja okna glownego
    #global ramka
    stworz(okno)

    screen = TurtleScreen(ramka)
    screen.bgcolor("gray")

    my_turtle = RawTurtle(screen)
    my_turtle.speed(7)

    my_turtle.pensize(1)
    my_turtle.hideturtle()
    my_turtle.penup()
    my_turtle.goto(-200,-100)
    my_turtle.pendown()

    my_turtle.fillcolor('green')
    my_turtle.begin_fill()
    my_turtle.goto(100,-100)
    my_turtle.goto(100,100)
    my_turtle.goto(-200,100)
    my_turtle.goto(-200,-100)
    my_turtle.end_fill()
    my_turtle.penup()
    my_turtle.goto(-50,-100)
    my_turtle.pendown()
    my_turtle.fillcolor('blue')
    my_turtle.begin_fill()
    my_turtle.goto(-50,0)
    my_turtle.goto(20,0)
    my_turtle.goto(20,-100)
    my_turtle.goto(-50,-100)
    my_turtle.end_fill()
    my_turtle.penup()
    my_turtle.goto(-200,100)
    my_turtle.pendown()

    my_turtle.fillcolor('brown')
    my_turtle.begin_fill()
    my_turtle.goto(-130,180)
    my_turtle.goto(170,180)
    my_turtle.goto(100,100)
    my_turtle.goto(-200,100)
    my_turtle.penup()
    my_turtle.goto(170,180)
    my_turtle.pendown()
    my_turtle.goto(250,110)
    my_turtle.goto(100,100)
    my_turtle.end_fill()

    my_turtle.fillcolor('green')
    my_turtle.begin_fill()
    my_turtle.goto(100,-100)
    my_turtle.goto(250,-90)
    my_turtle.goto(250,110)
    my_turtle.goto(100,100)
    my_turtle.end_fill()



    okno.mainloop()
