from tkinter import *
from tkinter import filedialog

root = Tk()
menubar = Menu(root)
root.config(menu=menubar)
root.title('Tk Menu')
root.geometry('150x150')

filemenu = Menu(menubar)
filemenu2 = Menu(menubar)
filemenu3 = Menu(menubar)

menubar.add_cascade(label='Arquivo', menu=filemenu)
menubar.add_cascade(label='Cores', menu=filemenu2)
menubar.add_cascade(label='Ajuda', menu=filemenu3)

def Open():
    filename = filedialog.askopenfilename()
    if filename:
        print(f'Opening file: {filename}')

def Save():
    filename = filedialog.asksaveasfilename()
    if filename:
        print(f'Saving file: {filename}')

def Quit():
    root.destroy()

def ColorBlue():
    root.configure(bg='blue')

def ColorRed():
    root.configure(bg='red')

def ColorBlack():
    root.configure(bg='black')

def Help():
    text = Text(root)
    text.pack()
    text.insert('insert', 'Ao clicar no botão da\n'
                           'respectiva cor, o fundo da tela\n'
                           'aparecerá na cor escolhida.')

filemenu.add_command(label='Abrir...', command=Open)
filemenu.add_command(label='Salvar como...', command=Save)
filemenu.add_separator()
filemenu.add_command(label='Sair', command=Quit)

filemenu2.add_command(label='Azul', command=ColorBlue)
filemenu2.add_command(label='Vermelho', command=ColorRed)
filemenu2.add_command(label='Preto', command=ColorBlack)

filemenu3.add_command(label='Ajuda', command=Help)
root.state("zoomed")
root.mainloop()
