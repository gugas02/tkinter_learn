from tkinter import *

i = Tk()

i.title("teste do Tk")

lbl1 = Label(i,text = "user")
lbl1.pack()
inp1 = Entry(i)
inp1.pack()
lbl2 = Label(i,text = "senha")
lbl2.pack()
inp2 = Entry(i)
inp2.pack()
entrar = Button(i,text = "entrar")
entrar.pack()

i.mainloop()