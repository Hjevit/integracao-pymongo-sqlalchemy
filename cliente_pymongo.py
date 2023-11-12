# Pymongo
import pymongo

# Dependências para conexão com AtlasDB
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Conectando com o banco de dados no AtlasDB
uri = "<URL do banco de dados no AtlasDB>"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.test


# Preparando os documentos
cliente = [
    {
        "nome": "Pablo Menezes",
        "cpf": "00000000000",
        "conta": [
            ["90022211"]
        ]
    },

    {
        "id":  "90022211",
        "tipo": "corrente",
        "id_cliente": 0,
        "saldo": 1000000
    }
]

# Enviando um documento ao banco de dados
posts = db.posts

result = posts.insert_many(cliente) 
