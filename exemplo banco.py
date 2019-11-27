#importamos a lib de acesso
import fdb #instalar o driver - download firebirdsql.org

#conectamos ao banco de dados
con = fdb.connect(host='localhost', database='C:/Projetos/FIREBIRDDATA/Besscontrol.FDB',user='sysdba',password='masterkey')
#buscamos o cursor
cur = con.cursor()
#executamos o select
cur.execute('SELECT * FROM clientes')

# cur.commit(); - Use para INSERT, UPDATE e DELETE

print ("\n\nRESULTADOS:\n")
print ("|ID\t|NOME\t\t|")

#percorremos todos os registros mostrando o nome retornado
for coluna in cur.fetchall():
    print ("|" + str(coluna[0]) + "\t|" + coluna[1] + "\t\t|\n")

#depois de retornarmos os dados, fechamos a conexÃ£o
con.close()
