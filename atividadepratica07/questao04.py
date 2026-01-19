import json

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            return dados_json
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado")

def escrever_arquivo(nome_arquivo, dados):
    try:
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, ident = 4)
    
    except FileNotFoundError:
        print(f"Arquivo: {nome_arquivo} não encontrado!")

dados = {
    "nome": "joão",
    "idade": 25,
    "cidade": "são paulo"
}

nome = input("Digite o nome do arquivo JSON: ")
print(escrever_arquivo(nome, dados))