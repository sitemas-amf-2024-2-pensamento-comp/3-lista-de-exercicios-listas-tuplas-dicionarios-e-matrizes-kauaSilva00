def maior_numero(lista):

    if not lista:
        return None  
    maior = lista[0]  
    for numero in lista:
        if numero > maior:
            maior = numero  
    return maior

lista1 = [3, 5, 7, 2, 8]
lista2 = [-1, -5, -3, -4]
lista3 = [10, 20, 30, 25]
lista4 = []

print("Maior número na lista1:", maior_numero(lista1))  
print("Maior número na lista2:", maior_numero(lista2))  
print("Maior número na lista4:", maior_numero(lista4))  
