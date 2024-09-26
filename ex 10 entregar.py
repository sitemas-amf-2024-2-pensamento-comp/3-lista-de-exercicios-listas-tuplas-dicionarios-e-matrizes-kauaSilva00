def media(lista):
    
    if not lista:
        return None  
    soma = sum(lista)  
    return soma / len(lista) 

lista1 = [10, 20, 30, 40, 50]
lista2 = [1, 2, 3, 4, 5]
lista3 = [-10, 0, 10]
lista4 = []

print("Média da lista1:", media(lista1)) 
print("Média da lista2:", media(lista2)) 
print("Média da lista3:", media(lista3))  
print("Média da lista4:", media(lista4))  