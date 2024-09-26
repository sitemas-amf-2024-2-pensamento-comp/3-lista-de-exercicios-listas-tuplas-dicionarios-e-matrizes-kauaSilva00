pares = []
impares = []

print("Digite 10 números:")
for _ in range(10):
    numero = int(input("Número: "))
    
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Números ímpares:", impares)

