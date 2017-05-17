from tkinter import *


class entrada(object):
    def __init__(self,i):
        self.lbl1 = Label(i, text="user")
        self.lbl1.pack()

        self.inp1 = Entry(i)
        self.inp1.pack()

        self.lbl2 = Label(i, text="senha")
        self.lbl2.pack()

        self.inp2 = Entry(i, show="*")
        self.inp2.pack()

        self.entrar = Button(i, text="entrar", command=self.login)
        self.entrar.pack(side=LEFT)

        self.entrar2 = Button(i, text="entrar", command=self.criar)
        self.entrar2.pack(side=RIGHT)

        self.lbl3 = Label(i, text="")
        self.lbl3.pack()
        self.aux = 0
        self.dict1 = {'gugas02': "123456"}

    def login(self):
        c = self.inp1.get()
        d = self.inp2.get()

        try:
            if self.dict1[c] == d:
                self.lbl3['text'] = "bem vindo"
                self.lbl3['fg'] = "blue"
        except:
            self.lbl3['text'] = "Usuário ou senha invalida"
            self.lbl3['fg'] = "red"


    def criar(self):
        if not self.aux:
            self.entrar2['bg'] = "black"
            self.entrar2['fg'] = "white"
            self.lbl1["fg"] = "green"
            self.lbl2["fg"] = "green"
            self.aux+=1
        elif self.aux:
            a = self.inp1.get()
            b = self.inp2.get()
            if not a  or not b:
                self.lbl3['text'] = "Nenhum dos campos pode estar vazio!"
                self.lbl3['fg'] = "red"
            else:
                try:
                    x = self.dict1[a]
                    self.lbl3['text'] = "conta ja existente"
                    self.lbl3['fg'] = "red"
                except:
                    self.dict1[a] = b
                    self.lbl3['text'] = "Conta criada com sucesso"
                    self.lbl3['fg'] = "blue"

a = Tk()
entrada(a)
a.title("teste do Tk")

a.mainloop()
