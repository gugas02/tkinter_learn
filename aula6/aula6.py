from tkinter import *

branco = '#ffffff'
arquivo = open("aula6.txt", 'r')
leitura = arquivo.readlines()
if leitura[0][0] == "T":
    leitura = True
else:
    leitura = False


class Entrada(object):
    def __init__(self, i):
        self.fonte = ("verdana", "20", "bold")
        self.logo = PhotoImage(file="imgs/bg_python.gif")
        self.entra = PhotoImage(file="imgs/b_entrar.ppm")
        self.cria = PhotoImage(file="imgs/b_criar.ppm")
        self.novo = PhotoImage(file="imgs/b_novo.ppm")
        # cria primeiro frame
        self.frame1 = Frame(i)
        self.frame1["bg"] = branco
        # cria segundo frame
        self.frame2 = Frame(i)
        self.frame2["bg"] = branco
        # cria terceiro frame
        self.frame3 = Frame(i)
        self.frame3["bg"] = branco
        # empacota os frames
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        # cria o label do logo
        self.lbl = Label(self.frame1, image=self.logo, bg=branco)
        # cria o label do usuario
        self.lbl1 = Label(self.frame1, text="User", bg=branco, font=self.fonte)
        # cria a entrada do usuario
        self.inp1 = Entry(self.frame1)
        # cria o label da senha
        self.lbl2 = Label(self.frame1, text="Senha", bg=branco, font=self.fonte)
        # cria a entrada da senha
        self.inp2 = Entry(self.frame1, show="*")
        # cria o checkbutton
        self.var = leitura
        self.cbs = False
        self.cb = Checkbutton(self.frame1, text="Lembrar-me", bg=branco, font=self.fonte, command=self.cbatv)
        # cria o botão de entrar
        self.entrar = Button(self.frame2, image=self.entra, command=self.login, bg=branco)
        # cria o botão de novo/criar
        self.entrar2 = Button(self.frame2, image=self.novo, command=self.criar, bg=branco)
        # empacota tudo
        self.lbl.pack()
        self.lbl1.pack()
        self.lbl3 = Label(self.frame3, text="")
        self.inp1.pack()
        self.lbl2.pack()
        self.inp2.pack()
        self.cb.pack()
        self.entrar.pack(side=LEFT)
        self.entrar2.pack(side=LEFT)
        self.lbl3.pack()
        if self.var:
            self.inp1.insert(END, "gugas02")
            self.inp2.insert(END, "123456")
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
            self.entrar2['fg'] = "white"
            self.entrar2['image'] = self.cria
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

    def cbatv(self):
        self.cbs = not self.cbs
        if self.cbs:
            arquivo = open("aula6.txt", 'w')
            arquivo.writelines('True')
        else:
            arquivo = open("aula6.txt", 'w')
            arquivo.writelines('False')

inter = Tk()
inter['bg'] = branco
Entrada(inter)
inter.title("teste do Tk")

inter.mainloop()
