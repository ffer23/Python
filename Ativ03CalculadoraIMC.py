"""
CALCULADORA IMC
"""

#!/usr/bin/env python
# -*- coding: latin1 -*-

from tkinter import*

root = Tk()


def calcular():
    if str(txtPeso.get()).isnumeric() and str(txtAltura.get()).isnumeric():
        peso = float(txtPeso.get())
        altura = float(txtAltura.get())/100
        res = peso / (altura * altura)
        lblResposta["text"] = res

    if res < 17:
        lblAnalise["text"] = "Muito abaixo do peso"
    elif res >= 17 and res < 18.49:
        lblAnalise["text"] = "Abaixo do peso"
    elif res >= 18.50 and res < 24.99:
        lblAnalise["text"] = "Peso normal"
    elif res >= 25 and res < 29.99:
        lblAnalise["text"] = "Acima do peso"
    elif res >= 30 and res < 34.99:
        lblAnalise["text"] = "Obesidade I"
    elif res >= 35 and res < 39.99:
        lblAnalise["text"] = "Obesidade II (severa)"
    else:
        lblAnalise["text"] = "Obesidade III (mórbida)"


def reiniciar():
    txtNome.delete(0, END)
    txtEnd.delete(0, END)
    txtPeso.delete(0, END)
    txtAltura.delete(0, END)
    lblResposta["text"] = "0"
    lblAnalise["text"] = " "


def sair():
    root.destroy()
    return


root.geometry("550x200")
root.title("Cálculo do IMC - Índice de Massa Corporal")
root.configure(background='WHITE')

MargemT = Frame(root, width=600, height=10)
MargemT.pack(side=TOP, fill=BOTH, expand=0)

MargemB = Frame(root, width=600, height=50)
MargemB.pack(side=BOTTOM, fill=BOTH, expand=0)

MargemR = Frame(root, width=10, height=200)
MargemR.pack(side=RIGHT, fill=BOTH, expand=0)

MargemL = Frame(root, width=10, height=200)
MargemL.pack(side=LEFT, fill=BOTH, expand=0)

Top = Frame(root, width=580, height=70)
Top.pack(side=TOP, fill=BOTH, expand=2)

Bottom = Frame(root, width=580, height=70)
Bottom.pack(side=BOTTOM, fill=BOTH, expand=3)

BottomR = Frame(Bottom, width=290, height=70, bd=4, relief="raise")
BottomR.pack(side=RIGHT, fill=BOTH, expand=2)

BottomL = Frame(Bottom, width=290, height=70)
BottomL.pack(side=LEFT, fill=BOTH, expand=1)

lblNome = Label(Top, font=('arial', 10), text="Nome do Paciente:  ", width=15, justify='left')
lblNome.grid(row=0, column=0, columnspan=1)

txtNome = Entry(Top, font=('arial', 10), bd=2, width=65, justify='left', state=NORMAL)
txtNome.grid(row=0, column=1, sticky=W+E)
txtNome.get()

lblEnd = Label(Top, font=('arial', 10), text="Endereço Completo:", width=15, justify='left')
lblEnd.grid(row=1, column=0, columnspan=1)

txtEnd = Entry(Top, font=('arial', 10), bd=2, width=65, justify='left', state=NORMAL)
txtEnd.grid(row=1, column=1, sticky=W+E)
txtEnd.get()

lblAltura = Label(BottomL, font=('arial', 10), text="Altura (cm)              ", width=15, justify='left')
lblAltura.grid(row=0, column=0, columnspan=1)

txtAltura = Entry(BottomL, font=('arial', 10), bd=2, width=40, justify='left', state=NORMAL)
txtAltura.grid(row=0, column=1)

lblPeso = Label(BottomL, font=('arial', 10), text="Peso (Kg)               ", width=15, justify='left')
lblPeso.grid(row=1, column=0, columnspan=1, sticky=W+E)

txtPeso = Entry(BottomL, font=('arial', 10), bd=2, width=40, justify='left', state=NORMAL)
txtPeso.grid(row=1, column=1)

bt1 = Button(MargemB, width=20, text="Calcular", bd=4, relief="raise", command=calcular).grid(row=1, column=1)

bt2 = Button(MargemB, width=20, text="Reiniciar", bd=4, relief="raise", command=reiniciar).grid(row=1, column=3)

lblResult = Label(BottomR, font=('arial', 13, 'bold'), text="Resultado")
lblResult.pack(side=TOP, fill=BOTH, expand=2)

lblResposta = Label(BottomR, font=('arial', 13, 'bold'), text="0")
lblResposta.pack(side=TOP, fill=BOTH, expand=2)

lblAnalise = Label(BottomR, font=('arial', 13, 'bold'), text=" ")
lblAnalise.pack(side=BOTTOM, fill=BOTH, expand=2)

bt3 = Button(MargemB, width=20, text="Sair", bd=4, relief="raise", command=sair).grid(row=1, column=5)

root.mainloop()
