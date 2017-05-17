from tkinter import *


def login():
    a = inp1.get()
    b = inp2.get()
    if a == 'gugas02' and b == "123456":
        lbl3['text'] = "bem vindo guh"
        lbl3['fg'] = "blue"
    else:
        lbl3['text'] = "Usuário ou senha invalida"
        lbl3['fg'] = "red"
i = Tk()

i.title("teste do Tk")

lbl1 = Label(i, text="user")
lbl1.pack()
inp1 = Entry(i)
inp1.pack()
lbl2 = Label(i, text="senha")
lbl2.pack()
inp2 = Entry(i)
inp2.pack()
entrar = Button(i, text="entrar", command=login)
entrar.pack()
lbl3 = Label(i, text="")
lbl3.pack()

i.mainloop()
