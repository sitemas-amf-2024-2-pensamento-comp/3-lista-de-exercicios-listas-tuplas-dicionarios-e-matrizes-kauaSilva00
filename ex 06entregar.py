lista1 = []
lista2 = []

print("Digite 5 números para a primeira lista:")
for _ in range(5):
    numero = float(input("Número: "))
    lista1.append(numero)

print("Digite 5 números para a segunda lista:")
for _ in range(5):
    numero = float(input("Número: "))
    lista2.append(numero)

lista_combinada = lista1 + lista2

print("Lista combinada:", lista_combinada)