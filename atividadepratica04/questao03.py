while True:
    try:

        senha = input("Digite a sua senha: ")

        if senha.lower() == 'sair':
            print("Saindo do programa")
            break

        if len(senha) < 8:
            raise Exception("A senha deve ter pelo menos 8 caracteres.")
        
        tem_numero = False
        for caractere in senha:
            if caractere in '0123456789':
                tem_numero = True
                break

        if tem_numero == False:
            raise Exception("A senha deve conter apenas um número")
        
        print("Senha válida")
        break

    except Exception as e:
        print(f"Erro {e} Tente novamente!")