numeros = []

for _ in range(10):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

print("O maior número é:", max(numeros))
print("O menor número é:", min(numeros))