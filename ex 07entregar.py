lista1 = []
lista2 = []

for _ in range(5):
    numero = float(input("Número: "))
    lista1.append(numero)

print("Digite 5 números para a segunda lista:")
for _ in range(5):
    numero = float(input("Número: "))
    lista2.append(numero)

elementos_comuns = []

for numero in lista1:
    if numero in lista2 and numero not in elementos_comuns:
        elementos_comuns.append(numero)

print("Elementos comuns:", elementos_comuns)