import mysql.connector
import conexaoBD #classe que conecta com o banco de dados

db_connection = conexaoBD.conectar()
con = db_connection.cursor()

def inserir(nome, telefone, endereco, dataDeNascimento):
    try:
        sql = "insert into pessoa(codigo,nome,telefone,endereco,dataDeNascimento) values ('', '{}', '{}', '{}', '{}')".format(nome, telefone, endereco, tratarData(dataDeNascimento))
        con.execute(sql)
        db_connection.commit() #Inserção no banco de dados via commit
        print ("{} Inseridos".format(con.rowcount)) #rowcount mostra quantas linhas foram afetadas

    except Exception as erro:
        return erro

def tratarData(texto):
    separado = texto.split('/')#divide um dado inserido apartir da indicação desejada, neste caso /
    dia = separado[0]
    mes = separado[1]
    ano = separado[2]
    return '{}-{}-{}'.format(ano,mes,dia)

def consultar():
    try:
        sql= 'select * from pessoa'
        con.execute(sql)

        for(codigo, nome, telefone, endereco, dataDeNascimento) in con:
            print('Codigo: {}, Nome: {}, Telefone: {}, Endereco: {}, Data de Nascimento: {}'.format(codigo, nome, telefone, endereco, dataDeNascimento))
        print('\n')
    except Exception as erro:
        print (erro)