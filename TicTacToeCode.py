from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import sys

tablero = Tk()
tablero.resizable(width=False,height=False)
tablero.title("Juego del gato")
tablero.configure(background="dark slate gray")

jug1=""
jug2=""
decision=True
turno=0
answer=True
cont=0
var=False

def main():
    botones=[]
    interno=[]
    turnojug=StringVar()
    xoxo=StringVar()
    for i in range(0,9,1):
        interno.append("V")

    btn1 = Button(tablero, text=" ", font='Times 20 bold', bg='black', fg='green2', height=4, width=8, command=lambda: valor(0,botones,interno,turnojug,xoxo))
    btn1.grid(row=1, column=0)
    botones.append(btn1)

    btn2 = Button(tablero, text=' ', font='Times 20 bold', bg='black', fg='green2', height=4, width=8, command=lambda: valor(1,botones,interno,turnojug,xoxo))
    btn2.grid(row=1, column=1)
    botones.append(btn2)

    btn3 = Button(tablero, text=' ',font='Times 20 bold', bg='black', fg='green2', height=4, width=8, command=lambda: valor(2,botones,interno,turnojug,xoxo))
    btn3.grid(row=1, column=2)
    botones.append(btn3)

    btn4 = Button(tablero, text=' ', font='Times 20 bold', bg='black', fg='green2', height=4, width=8, command=lambda: valor(3,botones,interno,turnojug,xoxo))
    btn4.grid(row=2, column=0)
    botones.append(btn4)

    btn5 = Button(tablero, text=' ', font='Times 20 bold', bg='black', fg='green2', height=4, width=8, command=lambda: valor(4,botones,interno,turnojug,xoxo))
    btn5.grid(row=2, column=1)
    botones.append(btn5)

    btn6 = Button(tablero, text=' ', font='Times 20 bold', bg='black', fg='green2', height=4, width=8, command=lambda: valor(5,botones,interno,turnojug,xoxo))
    btn6.grid(row=2, column=2)
    botones.append(btn6)

    btn7 = Button(tablero, text=' ', font='Times 20 bold', bg='black', fg='green2', height=4, width=8, command=lambda: valor(6,botones,interno,turnojug,xoxo))
    btn7.grid(row=3, column=0)
    botones.append(btn7)

    btn8 = Button(tablero, text=' ', font='Times 20 bold', bg='black', fg='green2', height=4, width=8, command=lambda: valor(7,botones,interno,turnojug,xoxo))
    btn8.grid(row=3, column=1)
    botones.append(btn8)

    btn9 = Button(tablero, text=' ', font='Times 20 bold', bg='black', fg='green2', height=4, width=8, command=lambda: valor(8,botones,interno,turnojug,xoxo))
    btn9.grid(row=3, column=2)
    botones.append(btn9)

    turnombre = Label(tablero,textvariable=turnojug,bd=5,height=2, width=16,bg="dark slate gray",fg='azure',font=('trebuchet ms',10,'bold'))
    turnombre.grid(row=0,column=1,columnspan=1)
    
    turnoxoxo = Label(tablero,textvariable=xoxo,bd=5,height=2, width=16,bg="dark slate gray",fg='azure',font=('trebuchet ms',10,'bold'))
    turnoxoxo.grid(row=0,column=0,columnspan=1)

    btninicio = Button(tablero, text='Jugar', font='arial 19 bold', bg='gold', fg='gray7', height=1, width=8, command=lambda: inicio_juego(botones,interno,turnojug,xoxo))#, command=lambda: click_boton(btn9))
    btninicio.grid(row=0, column=2)
    
    bloquear_btns(botones)

def bloquear_btns(botones):
    ''' '''
    for i in range(0,9):
        botones[i].configure(state=DISABLED)

def inicio_juego(botones,interno,turnojug,xoxo):
    ''' '''
    for i in range(0,9):
        botones[i].configure(state=NORMAL)
        botones[i].configure(bg='black')
        botones[i].configure(text="")
        interno[i] = "V"
    global jug1,jug2
    jug1 = simpledialog.askstring("Jugador X","Escribe tu nombre ")
    jug2 = simpledialog.askstring("Jugador O","Escribe tu nombre ")
    turnojug.set("Turno de " + jug1)
    xoxo.set("X")
    
def valor(num,botones,interno,turnojug,xoxo):
    ''' '''
    global turno,jug1,jug2,cont,var
    var=False
    if interno[num] == "V" and turno==0:
        botones[num].configure(text="X")
        botones[num].configure(bg="navy")
        interno[num] = "X"
        cont+=1
        turno = 1
        var = ganador(interno,botones,cont,xoxo)
        turnojug.set("Turno de " + jug2)
        xoxo.set("O")
    elif interno[num] == "V" and turno ==1:
        botones[num].configure(text="O")
        botones[num].configure(bg="brown4")
        interno[num] = "O"
        cont+=1
        turno = 0
        var = ganador(interno,botones,cont,xoxo)
        turnojug.set("Turno de " + jug1)
        xoxo.set("X")
    botones[num].configure(state=DISABLED)
    #if var==False:
        #seguir(interno,botones,xoxo,turnojug)
        
def ganador(interno,botones,cont,xoxo):
    ''' '''
    global var
    if (interno[0] == 'X' and interno[1] == 'X' and interno[2] == 'X' or
    interno[3] == 'X' and interno[4] == 'X' and interno[5] == 'X' or
    interno[6] == 'X' and interno[7] == 'X' and interno[8] == 'X' or
    interno[0] == 'X' and interno[3] == 'X' and interno[6] == 'X' or
    interno[1] == 'X' and interno[4] == 'X' and interno[7] == 'X' or
    interno[2] == 'X' and interno[5] == 'X' and interno[8] == 'X' or
    interno[0] == 'X' and interno[4] == 'X' and interno[8] == 'X' or
    interno[2] == 'X' and interno[4] == 'X' and interno[6] == 'X'):
        bloquear_btns(botones)
        messagebox.showinfo("¡Felicidades!","Ha ganado " + jug1 + ".")
        var=True
        denuevo(decision,xoxo)
    elif (interno[0] == 'O' and interno[1] == 'O' and interno[2] == 'O' or
    interno[3] == 'O' and interno[4] == 'O' and interno[5] == 'O' or
    interno[6] == 'O' and interno[7] == 'O' and interno[8] == 'O' or
    interno[0] == 'O' and interno[3] == 'O' and interno[6] == 'O' or
    interno[1] == 'O' and interno[4] == 'O' and interno[7] == 'O' or
    interno[2] == 'O' and interno[5] == 'O' and interno[8] == 'O' or
    interno[0] == 'O' and interno[4] == 'O' and interno[8] == 'O' or
    interno[2] == 'O' and interno[4] == 'O' and interno[6] == 'O'):
        bloquear_btns(botones)
        messagebox.showinfo("¡Felicidades!","Ha ganado " + jug2 + ".")
        denuevo(decision,xoxo)
        var=True
    elif(cont==9):
        messagebox.showinfo("¡Ups!","El juego ha terminado en empate.")
        denuevo(decision,xoxo)
        var=True
    return var

def denuevo(decision,xoxo):
    global cont,turno
    cont=0
    turno=0
    decision = messagebox.askyesno("¿Uno más?","¿Desea jugar de nuevo?")
    if decision==True:
        xoxo.set("X")
        main()
    else:
        messagebox.showinfo("¡Gracias por jugar!","Vuelve pronto por la revancha.")
        sys.exit()

def seguir(interno,botones,xoxo,turnojug):
    global jug2,decision
    answer = messagebox.askyesno("¿Algo no cuadra?", "¿Quiere seguir jugando?")
    if answer==False:
        palabra= str(xoxo.get())
        messagebox.showinfo("Juego detenido","El juego fue detenido por el jugador " + palabra + ".")
        denuevo(decision,xoxo)
main()
tablero.mainloop()
