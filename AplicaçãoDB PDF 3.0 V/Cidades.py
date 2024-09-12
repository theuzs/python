
from Banco import Banco

class Cidades:
    def __init__(self, idcidade=0, nome="", estado="", pais=""):
        self.idcidade = idcidade
        self.nome = nome
        self.estado = estado
        self.pais = pais

    def insertCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            INSERT INTO cidades (nome, estado, pais)
            VALUES (?, ?, ?)
            """, (self.nome, self.estado, self.pais))
            banco.conexao.commit()
            c.close()
            return "Cidade cadastrada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na inserção da cidade: {e}"

    def updateCidade(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("""
            UPDATE cidades
            SET nome = ?, estado = ?, pais = ?
            WHERE idcidade = ?
            """, (self.nome, self.estado, self.pais, self.idcidade))
            banco.conexao.commit()
            c.close()
            return "Cidade atualizada com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na alteração da cidade: {e}"

    def cidade_associada(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT COUNT(*) FROM clientes WHERE cidades = ?", (self.nome,))
            count = c.fetchone()[0]
            c.close()
            return count > 0
        except Exception as e:
            return f"Erro ao verificar associação: {e}"

    def deleteCidade(self):
        banco = Banco()
        try:
            # Verifica se a cidade está associada a algum cliente
            if self.cidade_associada():
                return "Não é possível excluir a cidade porque ela está associada a um ou mais clientes."

            # Se não estiver associada, procede com a exclusão
            c = banco.conexao.cursor()
            c.execute("DELETE FROM cidades WHERE idcidade = ?", (self.idcidade,))
            banco.conexao.commit()
            c.close()
            return "Cidade excluída com sucesso!"
        except Exception as e:
            return f"Ocorreu um erro na exclusão da cidade: {e}"

    def selectCidade(self, idcidade):
        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM cidades WHERE idcidade = ?", (idcidade,))
            row = c.fetchone()
            if row:
                self.idcidade, self.nome, self.estado, self.pais = row
            c.close()
            return "Busca feita com sucesso!" if row else "Cidade não encontrada."
        except Exception as e:
            return f"Ocorreu um erro na busca da cidade: {e}"

    def carregarCidades(self):
        for i in self.tree_cidades.get_children():
            self.tree_cidades.delete(i)

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM cidades")
            rows = c.fetchall()

            for row in rows:
                self.tree_cidades.insert("", "end", values=(row[0], row[1], row[2]))

            c.close()
        except Exception as e:
            print(f"Erro ao carregar cidades: {e}")

    def carregarClientes(self):
        for i in self.tree_clientes.get_children():
            self.tree_clientes.delete(i)

        banco = Banco()
        try:
            c = banco.conexao.cursor()
            c.execute("SELECT * FROM clientes")
            rows = c.fetchall()

            for row in rows:
                self.tree_clientes.insert("", "end", values=(row[0], row[1], row[2], row[3]))

            c.close()
        except Exception as e:
            print(f"Erro ao carregar clientes: {e}")
