from tkinter import *
largura = 500
altura = 500
canvas_l = 400
canvas_a = 400
branco = '#ffffff'
arquivo = open("aula6.txt", 'r')
leitura = arquivo.readlines()
if leitura[0][0] == "T":
    leitura = True
else:
    leitura = False


class Entrada(object):
    def __init__(self, i):
        self.i = i
        self.fonte = ("verdana", "20", "bold")
        self.logo = PhotoImage(file="imgs/bg_python.gif")
        self.entra = PhotoImage(file="imgs/b_entrar.ppm")
        self.cria = PhotoImage(file="imgs/b_criar.ppm")
        self.novo = PhotoImage(file="imgs/b_novo.ppm")
        self.cria_elementos2()
        self.x = 200
        self.y = 200


    def cria_elementos(self):
        # cria primeiro frame
        self.frame1 = Frame(self.i)
        self.frame1["bg"] = branco
        # cria segundo frame
        self.frame2 = Frame(self.i)
        self.frame2["bg"] = branco
        # cria 4 frame
        self.frame4 = Frame(self.i)
        self.frame4["bg"] = branco
        # cria 5 frame
        self.frame5 = Frame(self.i)
        self.frame5["bg"] = branco
        # cria 6 frame
        self.frame6 = Frame(self.i)
        self.frame6["bg"] = branco

        # empacota os frames
        self.frame4.pack()
        self.frame1.pack()
        self.frame5.pack()
        self.frame6.pack()
        self.frame2.pack()
        # cria o label do usuario
        self.lbl1 = Label(self.frame1, text="User", bg=branco, font=self.fonte)
        # cria a entrada do usuario
        self.inp1 = Entry(self.frame1)
        # cria o label da senha
        self.lbl2 = Label(self.frame1, text="Senha", bg=branco, font=self.fonte)
        # cria a entrada da senha
        self.inp2 = Entry(self.frame1, show="*")
        # cria o label do email
        self.lbl3 = Label(self.frame5, text="email", bg=branco, fg="green", font=self.fonte)
        # cria a entrada do email
        self.inp3 = Entry(self.frame5)
        # cria o label da nome
        self.lbl4 = Label(self.frame4, text="nome", bg=branco, fg="green", font=self.fonte)
        # cria a entrada da nome
        self.inp4 = Entry(self.frame4)
        # cria o botão de novo/criar
        self.entrar2 = Button(self.frame2, image=self.novo, command=self.criar, bg=branco)
        # empacota tudo
        self.lbl1.pack()
        self.inp1.pack()
        self.lbl2.pack()
        self.inp2.pack()
        self.lbl3.pack()
        self.inp3.pack()
        self.lbl4.pack()
        self.inp4.pack()
        self.entrar2.pack(side=LEFT)

    def cria_elementos2(self):
        self.frame0 = Frame(self.i)
        self.frame0["bg"] = branco
        # cria primeiro frame
        self.frame1 = Frame(self.i)
        self.frame1["bg"] = branco
        # cria segundo frame
        self.frame2 = Frame(self.i)
        self.frame2["bg"] = branco
        # cria terceiro frame
        self.frame3 = Frame(self.i)
        self.frame3["bg"] = branco
        # cria 6 frame
        self.frame6 = Frame(self.i)
        self.frame6["bg"] = branco
        # empacota os frames
        self.frame0.pack()
        self.frame1.pack()
        self.frame6.pack()
        self.frame2.pack()
        self.frame3.pack()
        # cria o label do logo
        self.lbl = Label(self.frame0, image=self.logo, bg=branco)
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
        self.cb = Checkbutton(self.frame6, text="Lembrar-me", bg=branco, font=self.fonte, command=self.cbatv)
        # cria o botão de entrar
        self.entrar = Button(self.frame2, image=self.entra, command=self.login, bg=branco)
        # cria o botão de novo/criar
        self.entrar2 = Button(self.frame2, image=self.novo, command=self.criar, bg=branco)
        # cria o label de resposta
        self.lbl3 = Label(self.frame3, text="")
        # empacota tudo
        self.lbl.pack()
        self.lbl1.pack()
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

    def cria_elementos3(self):
        self.frame0 = Frame(self.i)
        self.frame0["bg"] = branco
        # empacota o frame
        self.frame0.pack()
        # cria um botão para o primeiro app
        self.first_app = Button(self.frame0, text="App Canvas 1 - Linhas", command=self.app1, bg=branco)
        # empacota o btn
        self.first_app.pack()

    def cria_elementos4(self):
        inter.geometry("%ix%i" % (largura, altura))
        self.frame0 = Frame(self.i)
        self.frame0["bg"] = branco
        # cria primeiro frame
        self.frame1 = Frame(self.i)
        self.frame1["bg"] = branco
        #cria um canvas
        self.canvas = Canvas(self.frame0, bg=branco, width=canvas_l, height=canvas_a)
        # cria o botão cima
        self.cima = Button(self.frame1, text="Cima", command=self.up, bg=branco)
        # cria o botão baixo
        self.baixo = Button(self.frame1, text="Baixo", command=self.down, bg=branco)
        # cria o botão esquerda
        self.esquerda = Button(self.frame1, text="Esquerda", command=self.left, bg=branco)
        # cria o botão direita
        self.direita = Button(self.frame1, text="Direita", command=self.right, bg=branco)
        # empacota tudo
        self.frame0.pack()
        self.frame1.pack()
        self.canvas.pack()
        self.cima.pack(side=LEFT)
        self.baixo.pack(side=LEFT)
        self.esquerda.pack(side=LEFT)
        self.direita.pack(side=LEFT)


        #destroi oq foi construido com cria_elementos
    def destroi(self):
        self.lbl1.destroy()
        self.inp1.destroy()
        self.lbl2.destroy()
        self.inp2.destroy()
        self.lbl3.destroy()
        self.inp3.destroy()
        self.lbl4.destroy()
        self.inp4.destroy()
        self.entrar2.destroy()
        self.frame1.destroy()
        self.frame5.destroy()
        self.frame6.destroy()
        self.frame2.destroy()

    # destroi oq foi construido com cria_elementos2
    def destroi2(self):
        self.lbl.destroy()
        self.lbl1.destroy()
        self.inp1.destroy()
        self.lbl2.destroy()
        self.inp2.destroy()
        self.cb.destroy()
        self.entrar.destroy()
        self.entrar2.destroy()
        self.lbl3.destroy()
        # empacota os frames
        self.frame0.destroy()
        self.frame1.destroy()
        self.frame6.destroy()
        self.frame2.destroy()
        self.frame3.destroy()

    # destroi oq foi construido com cria_elementos3
    def destroi3(self):
        self.frame0.destroy()
        self.first_app.destroy()
    # rotina de login
    def login(self):
        c = self.inp1.get()
        d = self.inp2.get()

        try:
            if self.dict1[c] == d:
                self.destroi2()
                self.cria_elementos3()
            else:
                self.lbl3['text'] = "Usuário ou senha invalida"
                self.lbl3['fg'] = "red"
        except:
            self.lbl3['text'] = "Usuário ou senha invalida"
            self.lbl3['fg'] = "red"
    # rotina para criação de uma nova conta
    def criar(self):
        if not self.aux:
            self.destroi2()
            self.cria_elementos()
            self.entrar2['fg'] = "white"
            self.entrar2['image'] = self.cria
            self.lbl1["fg"] = "green"
            self.lbl2["fg"] = "green"
            self.aux += 1
        elif self.aux:
            a = self.inp1.get()
            b = self.inp2.get()
            self.destroi()
            self.cria_elementos2()
            if not a or not b:
                self.lbl3['text'] = "Nenhum dos campos pode estar vazio!"
                self.lbl3['fg'] = "red"
            else:
                try:
                    x = self.dict1[a]
                    self.lbl3['text'] = "Conta ja existente"
                    self.lbl3['fg'] = "red"
                except:
                    self.dict1[a] = b
                    self.lbl3['text'] = "Conta criada com sucesso"
                    self.lbl3['fg'] = "blue"

    #rotina do check button
    def cbatv(self):
        self.cbs = not self.cbs
        if self.cbs:
            arquivo = open("aula6.txt", 'w')
            arquivo.writelines('True')
        else:
            arquivo = open("aula6.txt", 'w')
            arquivo.writelines('False')

    #rotina do botão do primeiro app
    def app1(self):
        self.destroi3()
        self.cria_elementos4()
    def up(self):
        self.canvas.create_line(self.x, self.y, self.x, self.y-20, fill="red")
        self.y -= 20
    def down(self):
        self.canvas.create_line(self.x, self.y, self.x, self.y+20, fill="blue")
        self.y += 20
    def left(self):
        self.canvas.create_line(self.x, self.y, self.x-20, self.y, fill="green")
        self.x -= 20
    def right(self):
        self.canvas.create_line(self.x, self.y, self.x+20, self.y, fill="orange")
        self.x += 20

inter = Tk()
inter['bg'] = branco
Entrada(inter)
inter.title("teste do Tk")

inter.mainloop()
