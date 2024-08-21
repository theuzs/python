import sqlite3


class Banco:
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTables()

    def createTables(self):
        try:
            with self.conexao as conn:
                c = conn.cursor()

                # Tabela Usuarios
                c.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    idusuario INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    telefone TEXT,
                    email TEXT,
                    usuario TEXT,
                    senha TEXT
                )
                """)

                # Tabela Cidades
                c.execute("""
                CREATE TABLE IF NOT EXISTS cidades (
                    idcidade INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    estado TEXT,
                    pais TEXT
                )
                """)

                # Tabela Clientes
                c.execute("""
                CREATE TABLE IF NOT EXISTS clientes (
                    idcliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT,
                    telefone TEXT,
                    email TEXT,
                    endereco TEXT,
                    idcidade INTEGER,
                    FOREIGN KEY (idcidade) REFERENCES cidades(idcidade)
                )
                """)

                conn.commit()
        except sqlite3.Error as e:
            print(f"Erro ao criar tabelas: {e}")

    def close(self):
        if self.conexao:
            self.conexao.close()
