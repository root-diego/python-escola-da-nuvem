import random
import string

def gerar_senha(tamnho_senha):
    caracteres = string.ascii_letters + string.digits + "@!#$&"
    senha = ''
    for i in range(tamnho_senha):
        senha += random.choice(caracteres)

    return senha

tamanho = int(input('Digite o tamanho da senha: '))
senha = gerar_senha(tamanho)
print(f'Senha: {senha}')