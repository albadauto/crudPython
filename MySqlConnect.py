import mysql.connector
import os

class MySqlConnect:

    def __init__(self):
        try:
            self.conexao = mysql.connector.Connect(host='localhost', user='root', password='', database='area51')
        except():
            print("Error")


    def Cadastrar(self, nome, email, endereco):
        try:
            query = "INSERT INTO tb_cliente(cliente_nome, cliente_email, cliente_endereco) VALUES (%s, %s, %s)"
            dados = (nome, email, endereco)
            self.conexao.cursor().execute(query, dados)
            self.conexao.commit()
            print("Salvo com sucesso")
        except():
            print('Erro')


    def Procurar(self):
        try:
            query = "SELECT * FROM tb_cliente"
            cursor = self.conexao.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                print("ID:", row[0])
                print("Nome:", row[1])
                print("Email:", row[2])
                print("Endereço:", row[3])
                print(os.linesep)
        except():
            print('Erro')
        finally:
            if self.conexao.is_connected():
                self.conexao.close()


    def Excluir(self, id):
        try:
            query = "DELETE FROM tb_cliente WHERE cliente_id = %s"
            dados = (id,)
            cursor = self.conexao.cursor()
            cursor.execute(query, dados)
            self.conexao.commit()
            print("Deletado com sucesso!")
        except():
            print('Erro')