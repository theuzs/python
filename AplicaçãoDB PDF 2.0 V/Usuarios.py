#Usuarios.py
from Banco import Banco

class Usuarios:
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            INSERT INTO usuarios (nome, telefone, email, usuario, senha)
            VALUES (?, ?, ?, ?, ?)
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha))
            banco.conexao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção do usuário: {e}"

    def updateUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            UPDATE usuarios
            SET nome = ?, telefone = ?, email = ?, usuario = ?, senha = ?
            WHERE idusuario = ?
            """, (self.nome, self.telefone, self.email, self.usuario, self.senha, self.idusuario))
            banco.conexao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração do usuário: {e}"

    def deleteUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("DELETE FROM usuarios WHERE idusuario = ?", (self.idusuario,))
            banco.conexao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão do usuário: {e}"

    def selectUser(self, idusuario):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM usuarios WHERE idusuario = ?", (idusuario,))
            row = c.fetchone()
            if row:
                self.idusuario, self.nome, self.telefone, self.email, self.usuario, self.senha = row
            c.close()
            return "Busca feita com sucesso!" if row else "Usuário não encontrado."
        except Exception as e:
            return f"Ocorreu um erro na busca do usuário: {e}"

    def carregarUsuarios(self):
        # Clear the Treeview before adding new data
        for i in self.tree_usuarios.get_children():
            self.tree_usuarios.delete(i)

        # Connect to the database
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM usuarios")
            rows = c.fetchall()

            # Add users to the Treeview
            for row in rows:
                self.tree_usuarios.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))

            c.close()
        except Exception as e:
            print(f"Erro ao carregar usuários: {e}")

    def carregarCidades(self):
        # Clear the Treeview before adding new data
        for i in self.tree_cidades.get_children():
            self.tree_cidades.delete(i)

        # Connect to the database
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM cidades")
            rows = c.fetchall()

            # Add cities to the Treeview
            for row in rows:
                self.tree_cidades.insert("", "end", values=(row[0], row[1], row[2]))

            c.close()
        except Exception as e:
            print(f"Erro ao carregar cidades: {e}")

    def carregarClientes(self):
        # Clear the Treeview before adding new data
        for i in self.tree_clientes.get_children():
            self.tree_clientes.delete(i)

        # Connect to the database
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM clientes")
            rows = c.fetchall()

            # Add clients to the Treeview
            for row in rows:
                self.tree_clientes.insert("", "end", values=(row[0], row[1], row[2], row[3]))

            c.close()
        except Exception as e:
            print(f"Erro ao carregar clientes: {e}")
