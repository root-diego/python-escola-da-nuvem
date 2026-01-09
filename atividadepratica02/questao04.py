distancia_percorrida = float(input("Digite a distância percorrida em KM: "))
combustivel_gasto = float(input("Digite o combustível gasto em litros: "))

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"Consumo médio: {consumo_medio:.2f} km/l")
print(f"Distância: {distancia_percorrida:.2f}")
print(f"Combustivel gasto: {combustivel_gasto:.2f} L")