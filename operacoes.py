import mysql.connector
import conexaoBD #classe que conecta com o banco de dados

db_connection = conexaoBD.conectar()
con = db_connection.cursor()

def inserir(nome, telefone, endereco, dataDeNascimento):
    try:
        sql = "insert into pessoa(codigo,nome,telefone,endereco,dataDeNascimento) values ('', '{}', '{}', '{}', '{}')".format(nome, telefone, endereco, dataDeNascimento)
        con.execute(sql)
        db_connection.commit() #Inserção no banco de dados via commit
        print ("{} Inseridos".format(con.rowcount)) #rowcount mostra quantas linhas foram afetadas

    except Exception as erro:
        return erro

