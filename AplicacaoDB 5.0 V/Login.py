from tkinter import *
from tkinter import messagebox
import sqlite3
from App import Application

class Login:
    def __init__(self, master=None):
        self.master = master
        self.master.title('Login')
#        self.master.geometry('400x450')
        self.master.configure(bg='#34495e')  # Fundo escuro e elegante


        self.logo_label = Label(master, text="🔒", font=("Helvetica", 48), bg='#34495e', fg='#ecf0f1')
        self.logo_label.pack(pady=(30, 10))

        # Frame central com cantos arredondados e sombras (simulação)
        self.central_frame = Frame(master, bg='#ecf0f1', borderwidth=0)
        self.central_frame.pack(pady=10, padx=40, fill=BOTH, expand=TRUE)

        # Título acima dos campos com sombra
        self.title_label = Label(self.central_frame, text="Bem-vindo !", font=("Helvetica", 18, "bold"),
                                 bg='#ecf0f1', fg='#2c3e50')
        self.title_label.pack(pady=(20, 10))

        # Campo de usuário
        self.username_label = Label(self.central_frame, text="Usuário", font=("Verdana", 12), bg='#ecf0f1',
                                    fg='#2c3e50')
        self.username_label.pack(pady=(10, 5))

        self.username_entry = Entry(self.central_frame, font=("Verdana", 12), bd=0, bg='#bdc3c7', fg='#2c3e50',
                                    relief="flat")
        self.username_entry.pack(pady=5, ipadx=10, ipady=7)

        # Campo de senha
        self.password_label = Label(self.central_frame, text="Senha", font=("Verdana", 12), bg='#ecf0f1', fg='#2c3e50')
        self.password_label.pack(pady=(10, 5))

        self.password_entry = Entry(self.central_frame, show="*", font=("Verdana", 12), bd=0, bg='#bdc3c7',
                                    fg='#2c3e50', relief="flat")
        self.password_entry.pack(pady=5, ipadx=10, ipady=7)

        # Botão de login com efeito de hover
        button_font = ("Verdana", 12, "bold")
        self.login_button = Button(self.central_frame, text="Entrar", font=button_font, bg='#e74c3c', fg='#ffffff',
                                   activebackground='#c0392b', activeforeground='#ffffff', bd=0, relief="flat",
                                   command=self.login)
        self.login_button.pack(pady=(30, 10), ipadx=10, ipady=7)

        # Efeito de hover no botão
        self.login_button.bind("<Enter>", lambda e: self.login_button.config(bg='#c0392b'))
        self.login_button.bind("<Leave>", lambda e: self.login_button.config(bg='#e74c3c'))

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE usuario = ? AND senha = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            self.master.destroy()  # Fecha a tela de login
            root = Tk()
            app = Application(master=root)  # Chama a aplicação principal
            root.state("zoomed")
            root.mainloop()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos")


if __name__ == "__main__":
    root = Tk()
    login_app = Login(master=root)
    root.state("zoomed")
    root.mainloop()