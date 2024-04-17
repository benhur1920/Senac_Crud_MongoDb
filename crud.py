# Importando biblioteca
import pymongo

#Conexão com o banco de dados
client = pymongo.MongoClient("localhost", 27017)

# Criar o banco de dados
db = client["Agenda"]

# Criar o documento/collection
colecao = db["contatos"]
documento = {"nome":"João", "sobrenome":"Silva", "idade": 30}
resultado = colecao.insert_one(documento)
print(resultado.inserted_id)

#ler um documento
filtro = {"nome":"João"}
resultado = colecao.find_one(filtro)
print(resultado)


#Atualizando um documento
#filtro = {"nome":"João"}
#atualizacoes = {"$set":{"idade":31}}
#resultado = colecao.update_one(filtro, atualizacoes)
#print(resultado.modified_count)
print(resultado)


#Excluindo um documento
#filtro = {"nome":"João"}
#resultado = colecao.delete_one(filtro)