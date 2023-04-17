# importando o Modulo
from pymongo import MongoClient

#Conectando ao MongoDB
conn = MongoClient('localhost', 27017)

# Conectando ao banco de dados
db = conn.ecommerce


# Criando uma Collection na Base de Dados Chamada Produtos.
col_produtos = db.produtos

prod1 =   {  "_id": 1,
                "Nome": "SmartPhone",
                "Fabricante": "Samsung",
                "valor": 3500.90,
                "estoque": 10
}

prod2 =   {  "_id": 2,
                "Nome": "Televisão",
                "Fabricante": "LG",
                "valor": 2500,
                "estoque": 20
}


#Inserindo os dados na collection

col_produtos.insert_one(prod1)

# Testando se inseriu com comando FindOne

print(col_produtos.find_one({}))

# Adicionando Segundo Produto

col_produtos.insert_one(prod2)

# Criando um cursor para repetir as operações de consulta e executando 
# com laço for

for doc in col_produtos.find():
    print(doc)


