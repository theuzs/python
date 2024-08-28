from tkinter import *
from tkinter import ttk
from Usuarios import Usuarios
from Cidades import Cidades
from Clientes import Clientes
import sqlite3

class Application:
    def __init__(self, master=None):
        self.master = master
        self.master.title('Tela Principal')
        self.master.geometry('800x600')

        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=BOTH, expand=TRUE)

        self.frame_usuarios = Frame(self.notebook)
        self.frame_cidades = Frame(self.notebook)
        self.frame_clientes = Frame(self.notebook)

        self.notebook.add(self.frame_usuarios, text='Usuários')
        self.notebook.add(self.frame_cidades, text='Cidades')
        self.notebook.add(self.frame_clientes, text='Clientes')

        self.add_usuarios_content()
        self.add_cidades_content()
        self.add_clientes_content()

    def add_usuarios_content(self):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(self.frame_usuarios, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container4.pack()

        self.container5 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container5.pack()

        self.container6 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(self.frame_usuarios, padx=20, pady=5)
        self.container7.pack()

        self.container8 = Frame(self.frame_usuarios, padx=20, pady=10)
        self.container8.pack()

        self.container9 = Frame(self.frame_usuarios, pady=15)
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados:", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        self.lblidusuario = Label(self.container2, text="ID Usuário:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)
        self.txtidusuario = Entry(self.container2, width=10, font=self.fonte)
        self.txtidusuario.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarUsuario)
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container3, width=25, font=self.fonte)
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.container4, width=25, font=self.fonte)
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        self.txtemail = Entry(self.container5, width=25, font=self.fonte)
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario = Entry(self.container6, width=25, font=self.fonte)
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container7, width=25, show="*", font=self.fonte)
        self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirUsuario)
        self.bntInsert.pack(side=LEFT)
        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12, command=self.alterarUsuario)
        self.bntAlterar.pack(side=LEFT)
        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12, command=self.excluirUsuario)
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsg.pack()
        columns = ("ID", "Nome", "Telefone", "Email")
        self.tree_usuarios = ttk.Treeview(self.frame_usuarios, columns=columns, show='headings')
        for col in columns:
            self.tree_usuarios.heading(col, text=col)
        self.tree_usuarios.pack(fill=BOTH, expand=True)

        # Fetch and populate data
        data = self.fetch_usuarios_data()
        self.populate_treeview(self.tree_usuarios, data)

    def add_cidades_content(self):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(self.frame_cidades, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container4.pack()

        self.container5 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container5.pack()

        self.container6 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(self.frame_cidades, padx=20, pady=5)
        self.container7.pack()

        self.container8 = Frame(self.frame_cidades, padx=20, pady=10)
        self.container8.pack()

        self.container9 = Frame(self.frame_cidades, pady=15)
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados:", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        self.lblidcidade = Label(self.container2, text="ID Cidade:", font=self.fonte, width=10)
        self.lblidcidade.pack(side=LEFT)
        self.txtidcidade = Entry(self.container2, width=10, font=self.fonte)
        self.txtidcidade.pack(side=LEFT)
        self.btnBuscarCidade = Button(self.container2, text="Buscar", font=self.fonte, width=10, command=self.buscarCidade)
        self.btnBuscarCidade.pack(side=RIGHT)

        self.lblnomecidade = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnomecidade.pack(side=LEFT)
        self.txtnomecidade = Entry(self.container3, width=25, font=self.fonte)
        self.txtnomecidade.pack(side=LEFT)

        self.lblestado = Label(self.container4, text="Estado:", font=self.fonte, width=10)
        self.lblestado.pack(side=LEFT)
        self.txtestado = Entry(self.container4, width=25, font=self.fonte)
        self.txtestado.pack(side=LEFT)

        self.lblpais = Label(self.container5, text="País:", font=self.fonte, width=10)
        self.lblpais.pack(side=LEFT)
        self.txtpais = Entry(self.container5, width=25, font=self.fonte)
        self.txtpais.pack(side=LEFT)

        self.bntInsertCidade = Button(self.container8, text="Inserir", font=self.fonte, width=12, command=self.inserirCidade)
        self.bntInsertCidade.pack(side=LEFT)
        self.bntAlterarCidade = Button(self.container8, text="Alterar", font=self.fonte, width=12, command=self.alterarCidade)
        self.bntAlterarCidade.pack(side=LEFT)
        self.bntExcluirCidade = Button(self.container8, text="Excluir", font=self.fonte, width=12, command=self.excluirCidade)
        self.bntExcluirCidade.pack(side=LEFT)

        self.lblmsgCidade = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsgCidade.pack()
        columns = ("ID", "Nome", "Estado", "País")
        self.tree_cidades = ttk.Treeview(self.frame_cidades, columns=columns, show='headings')
        for col in columns:
            self.tree_cidades.heading(col, text=col)
        self.tree_cidades.pack(fill=BOTH, expand=True)

        # Fetch and populate data
        data = self.fetch_cidades_data()
        self.populate_treeview(self.tree_cidades, data)

    def add_clientes_content(self):
        self.fonte = ("Verdana", "8")

        # Create frames for layout
        self.container1 = Frame(self.frame_clientes, pady=10)
        self.container1.pack()

        self.container2 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container2.pack()

        self.container3 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container3.pack()

        self.container4 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container4.pack()

        self.container5 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container5.pack()

        self.container6 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container6.pack()

        self.container7 = Frame(self.frame_clientes, padx=20, pady=5)
        self.container7.pack()

        self.container8 = Frame(self.frame_clientes, padx=20, pady=10)
        self.container8.pack()

        self.container9 = Frame(self.frame_clientes, pady=15)
        self.container9.pack()

        # Add labels and entries
        self.titulo = Label(self.container1, text="Informe os dados:", font=("Calibri", "9", "bold"))
        self.titulo.pack()

        self.lblidcliente = Label(self.container2, text="ID Cliente:", font=self.fonte, width=10)
        self.lblidcliente.pack(side=LEFT)
        self.txtidcliente = Entry(self.container2, width=10, font=self.fonte)
        self.txtidcliente.pack(side=LEFT)
        self.btnBuscarCliente = Button(self.container2, text="Buscar", font=self.fonte, width=10,
                                       command=self.buscarCliente)
        self.btnBuscarCliente.pack(side=RIGHT)

        self.lblnomecliente = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnomecliente.pack(side=LEFT)
        self.txtnomecliente = Entry(self.container3, width=25, font=self.fonte)
        self.txtnomecliente.pack(side=LEFT)

        self.lbltelefonecliente = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefonecliente.pack(side=LEFT)
        self.txttelefonecliente = Entry(self.container4, width=25, font=self.fonte)
        self.txttelefonecliente.pack(side=LEFT)

        self.lblemailcliente = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemailcliente.pack(side=LEFT)
        self.txtemailcliente = Entry(self.container5, width=25, font=self.fonte)
        self.txtemailcliente.pack(side=LEFT)

        self.lblcidade = Label(self.container6, text="Cidade:", font=self.fonte, width=10)
        self.lblcidade.pack(side=LEFT)
        self.cidade_combobox = ttk.Combobox(self.container6, width=25, font=self.fonte)
        self.cidade_combobox.pack(side=LEFT)
        self.populate_cidade_combobox()

        # Add buttons
        self.bntInsertCliente = Button(self.container8, text="Inserir", font=self.fonte, width=12,
                                       command=self.inserirCliente)
        self.bntInsertCliente.pack(side=LEFT)
        self.bntAlterarCliente = Button(self.container8, text="Alterar", font=self.fonte, width=12,
                                        command=self.alterarCliente)
        self.bntAlterarCliente.pack(side=LEFT)
        self.bntExcluirCliente = Button(self.container8, text="Excluir", font=self.fonte, width=12,
                                        command=self.excluirCliente)
        self.bntExcluirCliente.pack(side=LEFT)

        self.lblmsgCliente = Label(self.container9, text="", font=("Verdana", "9", "italic"))
        self.lblmsgCliente.pack()

        # Configuring the Treeview
        columns = ("ID", "Nome", "Telefone", "Email", "Cidade")  # Added Cidade column
        self.treeview = ttk.Treeview(self.frame_clientes, columns=columns, show='headings')
        for col in columns:
            self.treeview.heading(col, text=col)

        self.treeview.pack(fill=BOTH, expand=True)

        # Fetch and populate data
        data = self.fetch_clientes_data()
        self.populate_treeview(self.treeview, data)

    def populate_cidade_combobox(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT nome FROM cidades")
        cidades = cursor.fetchall()
        conn.close()

        self.cidade_combobox['values'] = [cidade[0] for cidade in cidades]

    def inserirUsuario(self):
        user = Usuarios(nome=self.txtnome.get(), telefone=self.txttelefone.get(), email=self.txtemail.get(),
                        usuario=self.txtusuario.get(), senha=self.txtsenha.get())
        self.lblmsg["text"] = user.insertUser()
        self.limparCamposUsuario()
        self.refresh_usuarios_treeview()

    def alterarUsuario(self):
        user = Usuarios(idusuario=self.txtidusuario.get(), nome=self.txtnome.get(), telefone=self.txttelefone.get(),
                        email=self.txtemail.get(), usuario=self.txtusuario.get(), senha=self.txtsenha.get())
        self.lblmsg["text"] = user.updateUser()
        self.limparCamposUsuario()
        self.refresh_usuarios_treeview()

    def excluirUsuario(self):
        user = Usuarios(idusuario=self.txtidusuario.get())
        self.lblmsg["text"] = user.deleteUser()
        self.limparCamposUsuario()
        self.refresh_usuarios_treeview()

    def buscarUsuario(self):
        user = Usuarios()
        idusuario = self.txtidusuario.get()
        self.lblmsg["text"] = user.selectUser(idusuario)
        if user.idusuario:
            self.txtidusuario.delete(0, END)
            self.txtidusuario.insert(INSERT, user.idusuario)
            self.txtnome.delete(0, END)
            self.txtnome.insert(INSERT, user.nome)
            self.txttelefone.delete(0, END)
            self.txttelefone.insert(INSERT, user.telefone)
            self.txtemail.delete(0, END)
            self.txtemail.insert(INSERT, user.email)
            self.txtusuario.delete(0, END)
            self.txtusuario.insert(INSERT, user.usuario)
            self.txtsenha.delete(0, END)
            self.txtsenha.insert(INSERT, user.senha)
            self.refresh_usuarios_treeview()

    def limparCamposUsuario(self):
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

    def inserirCidade(self):
        cidade = Cidades(nome=self.txtnomecidade.get(), estado=self.txtestado.get(), pais=self.txtpais.get())
        self.lblmsgCidade["text"] = cidade.insertCidade()
        self.limparCamposCidade()
        self.refresh_cidades_treeview()

    def alterarCidade(self):
        cidade = Cidades(idcidade=self.txtidcidade.get(), nome=self.txtnomecidade.get(), estado=self.txtestado.get(), pais=self.txtpais.get())
        self.lblmsgCidade["text"] = cidade.updateCidade()
        self.limparCamposCidade()
        self.refresh_cidades_treeview()

    def excluirCidade(self):
        cidade = Cidades(idcidade=self.txtidcidade.get())
        self.lblmsgCidade["text"] = cidade.deleteCidade()
        self.limparCamposCidade()
        self.refresh_cidades_treeview()

    def buscarCidade(self):
        cidade = Cidades()
        idcidade = self.txtidcidade.get()
        self.lblmsgCidade["text"] = cidade.selectCidade(idcidade)
        if cidade.idcidade:
            self.txtidcidade.delete(0, END)
            self.txtidcidade.insert(INSERT, cidade.idcidade)
            self.txtnomecidade.delete(0, END)
            self.txtnomecidade.insert(INSERT, cidade.nome)
            self.txtestado.delete(0, END)
            self.txtestado.insert(INSERT, cidade.estado)
            self.txtpais.delete(0, END)
            self.txtpais.insert(INSERT, cidade.pais)
            self.refresh_cidades_treeview()

    def limparCamposCidade(self):
        self.txtidcidade.delete(0, END)
        self.txtnomecidade.delete(0, END)
        self.txtestado.delete(0, END)
        self.txtpais.delete(0, END)

    def inserirCliente(self):
        cliente = Clientes(nome=self.txtnomecliente.get(), telefone=self.txttelefonecliente.get(), email=self.txtemailcliente.get())
        self.lblmsgCliente["text"] = cliente.insertCliente()
        self.limparCamposCliente()
        self.refresh_clientes_treeview()

    def alterarCliente(self):
        cliente = Clientes(idcliente=self.txtidcliente.get(), nome=self.txtnomecliente.get(), telefone=self.txttelefonecliente.get(), email=self.txtemailcliente.get())
        self.lblmsgCliente["text"] = cliente.updateCliente()
        self.limparCamposCliente()
        self.refresh_clientes_treeview()

    def excluirCliente(self):
        cliente = Clientes(idcliente=self.txtidcliente.get())
        self.lblmsgCliente["text"] = cliente.deleteCliente()
        self.limparCamposCliente()
        self.refresh_clientes_treeview()

    def buscarCliente(self):
        cliente = Clientes()
        idcliente = self.txtidcliente.get()
        self.lblmsgCliente["text"] = cliente.selectCliente(idcliente)
        if cliente.idcliente:
            self.txtidcliente.delete(0, END)
            self.txtidcliente.insert(INSERT, cliente.idcliente)
            self.txtnomecliente.delete(0, END)
            self.txtnomecliente.insert(INSERT, cliente.nome)
            self.txttelefonecliente.delete(0, END)
            self.txttelefonecliente.insert(INSERT, cliente.telefone)
            self.txtemailcliente.delete(0, END)
            self.txtemailcliente.insert(INSERT, cliente.email)
            self.refresh_clientes_treeview()
            self.cidade_combobox.set(cliente.cidade)

    def limparCamposCliente(self):
        self.txtidcliente.delete(0, END)
        self.txtnomecliente.delete(0, END)
        self.txttelefonecliente.delete(0, END)
        self.txtemailcliente.delete(0, END)

    def populate_treeview(self, treeview, data):
        for row in data:
            treeview.insert("", "end", values=row)

    def fetch_data_c(self):
        conn = sqlite3.connect('banco.db')  # Conectando ao banco de dados
        cursor = conn.cursor()

        # Executando uma consulta SQL para pegar todos os dados da tabela
        cursor.execute("SELECT * FROM clientes")  # Adjust the query based on your actual table
        rows = cursor.fetchall()  # Buscando todos os resultados
        conn.close()

        return rows

    def fetch_usuarios_data(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def fetch_cidades_data(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cidades")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def fetch_clientes_data(self):
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes")
        rows = cursor.fetchall()
        conn.close()
        return rows

    def refresh_usuarios_treeview(self):
        data = self.fetch_usuarios_data()
        self.tree_usuarios.delete(*self.tree_usuarios.get_children())
        self.populate_treeview(self.tree_usuarios, data)

    def refresh_cidades_treeview(self):
        data = self.fetch_cidades_data()
        self.tree_cidades.delete(*self.tree_cidades.get_children())
        self.populate_treeview(self.tree_cidades, data)

    def refresh_clientes_treeview(self):
        data = self.fetch_clientes_data()
        self.treeview.delete(*self.treeview.get_children())
        self.populate_treeview(self.treeview, data)


if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    root.mainloop()
