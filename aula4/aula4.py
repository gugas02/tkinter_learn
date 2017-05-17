from tkinter import *


class Entrada(object):
    def __init__(self, i):
        # cria primeiro frame
        self.frame1 = Frame(i)
        # cria segundo frame
        self.frame2 = Frame(i)
        # cria terceiro frame
        self.frame3 = Frame(i)
        # empacota os frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        # cria o label do usuario
        self.lbl1 = Label(self.frame1, text="user")
        # cria a entrada do usuario
        self.inp1 = Entry(self.frame1)
        # cria o label da senha
        self.lbl2 = Label(self.frame1, text="senha")
        # cria a entrada da senha
        self.inp2 = Entry(self.frame1, show="*")
        # cria o botão de entrar
        self.entrar = Button(self.frame2, text="entrar", command=self.login)
        # cria o botão de novo/criar
        self.entrar2 = Button(self.frame2, text="novo", command=self.criar)
        # empacota tudo
        self.lbl1.pack()
        self.lbl3 = Label(self.frame3, text="")
        self.inp1.pack()
        self.lbl2.pack()
        self.inp2.pack()
        self.entrar.pack(side=LEFT)
        self.entrar2.pack(side=LEFT)
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
            else:
                self.lbl3['text'] = "Usuário ou senha invalida"
                self.lbl3['fg'] = "red"
        except:
            self.lbl3['text'] = "Usuário ou senha invalida"
            self.lbl3['fg'] = "red"

    def criar(self):
        if not self.aux:
            self.entrar2['bg'] = "black"
            self.entrar2['fg'] = "white"
            self.entrar2['text'] = "Criar!"
            self.lbl1["fg"] = "green"
            self.lbl2["fg"] = "green"
            self.aux += 1
        elif self.aux:
            a = self.inp1.get()
            b = self.inp2.get()
            if not a or not b:
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

inter = Tk()
Entrada(inter)
inter.title("teste do Tk")

inter.mainloop()
