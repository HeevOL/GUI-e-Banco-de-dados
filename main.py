from tkinter import *
from tkinter import ttk


def salva_dados():
    v1 = str(nome.get())
    v2 = configura_cpf(str(cpf.get()))
    v3 = str(matricula.get())
    v4 = configura_data(str(nasc_data.get()))

    arquivo = open('Aplicação GUI e manipulação de arquivos/bd.txt', 'a')
    arquivo.write(f'{v1}|{v2}|{v3}|{v4}\n')
    arquivo.close()

    save_button.configure(text="Dados Salvos!!")
    limpa_valores()


def listar_dados():
    arquivo = open('Aplicação GUI e manipulação de arquivos/bd.txt', 'r')
    bd = Tk()
    bd.title("Banco de dados")
    bd.geometry("600x400")
    
    tv = ttk.Treeview(bd,columns=('Nome', 'CPF', 'Matricula', 'Nascimento'), show='headings')
    tv.column('Nome', minwidth=0,width=250)
    tv.column('CPF', minwidth=0,width=100)
    tv.column('Matricula', minwidth=0,width=100)
    tv.column('Nascimento', minwidth=0,width=100)
    tv.heading('Nome', text='Nome')
    tv.heading('CPF', text='CPF')
    tv.heading('Matricula', text='Matricula')
    tv.heading('Nascimento', text='Nascimento')
    tv.pack()

    for dados in arquivo:
        lista = dados.split('|')
        tv.insert('','end',values=(lista[0],lista[1],lista[2],lista[3]))


def limpa_valores():
    nome.delete(0,'end')
    cpf.delete(0,'end')
    matricula.delete(0,'end')
    nasc_data.delete(0,'end')
    

def configura_cpf(cpf):
    if len(cpf) == 11:
        cpf = (cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:])
    return cpf


def configura_data(data):
    if len(data) == 8:
        data = (data[:2] + '/' + data[2:4] + '/' + data[4:])
    return data


window = Tk()
window.title("Formulário")
window.geometry("600x400")

lbl = Label(window, text="Olá! Preencha o formulário abaixo", font=("Helvetica",16))
lbl.place(x=10, y=10)

nome_lbl = Label(window, text="Nome:")
nome = Entry(window, bd=2)
nome_lbl.place(x=10, y=40)
nome.place(x=10, y=60, width=550)

cpf_lbl = Label(window, text="CPF:")
cpf = Entry(window, bd=2)
cpf_lbl.place(x=10,y=90)
cpf.place(x=10, y=110, width=300)

matricula_lbl = Label(window, text="Matricula:")
matricula = Entry(window, bd=2)
matricula_lbl.place(x=10, y=140)
matricula.place(x=10, y=160)

nasc_data_lbl = Label(window, text='Data de Nascimento:')
nasc_data = Entry(window, bd=2)
nasc_data_lbl.place(x=10, y=190)
nasc_data.place(x=10,y=210)

list_button = Button(window, text="Listar dados salvos", command=listar_dados)
list_button.pack(ipadx=20, ipady=5, padx=10, pady=10, side='bottom',fill=BOTH)
save_button = Button(window, text="Save", command=salva_dados)
save_button.pack(ipadx=20, ipady=5, padx=10, pady=10, side="bottom",fill=BOTH)

window.mainloop()