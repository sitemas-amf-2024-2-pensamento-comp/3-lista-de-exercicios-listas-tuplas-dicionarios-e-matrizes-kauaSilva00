def numeros_pares(lista):
    
    pares = [numero for numero in lista if numero % 2 == 0]
    return pares

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [11, 13, 15, 16, 18, 20]
lista3 = [0, -2, -3, -4, 5]

print("Números pares em lista1:", numeros_pares(lista1))  
print("Números pares em lista2:", numeros_pares(lista2))  
print("Números pares em lista3:", numeros_pares(lista3))  