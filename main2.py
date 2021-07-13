from MySqlConnect import *
import os

escolha = 0
print("BEM VINDO AO PROGRAMA" + os.linesep)
rodando = True
while rodando:
    mysql = MySqlConnect()
    escolha = int(input("SELECIONE UMA DAS ESCOLHAS: 1- Para cadastrar, 2- Para selecionar os clientes, 3- Para deletar, 0- Para sair: "))
    if escolha == 1:
        Nome = input("Digite o nome do cabra: ")
        Email = input("Agora o email!: ")
        Endereco = input("Boa! por ultimo agora, o endereco: ")
        mysql.Cadastrar(Nome, Email, Endereco)
    elif escolha == 2:
        mysql.Procurar()
    elif escolha == 3:
        ID = input("Digite o ID sem erros a ser deletado ")
        mysql.Excluir(ID)
    elif escolha == 0:
        rodando = False
    else:
        print("Por favor, digite um valor valido")



