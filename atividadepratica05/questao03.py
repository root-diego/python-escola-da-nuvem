def calcular_desconto(valor_produto, porcentagem_desconto):
    desconto = valor_produto * (porcentagem_desconto / 100)
    return desconto

valor_produto = float(input("Digite o valor do produto: "))
porcentagem_desconto = float(input("Digite a porcentagem do desconto: "))

desconto = calcular_desconto(valor_produto, porcentagem_desconto)

preco_final = valor_produto - desconto

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço final do produto: R$ {preco_final:.2f}")
