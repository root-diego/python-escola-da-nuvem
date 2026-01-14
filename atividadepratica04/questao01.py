while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, /, *): ")

        if operacao == "+":
            resultado = numero1 +numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "/":
            resultado = numero1 / numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        else:
            raise Exception()
        
        print("O resultado da operação é {resultado}")
        break
    
    except ValueError:
        print("Vocé deve digitar apenas números")
    except ZeroDivisionError:
        print("Não é possivel dividir por zero")
    except Exception:
        print("Operação inválida")