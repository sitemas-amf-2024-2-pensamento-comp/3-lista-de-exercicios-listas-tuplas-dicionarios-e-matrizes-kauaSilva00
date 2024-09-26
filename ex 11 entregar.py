def contar_elementos(lista, elemento):
 
    return lista.count(elemento)

lista1 = [1, 2, 3, 2, 4, 2, 5]
lista2 = ['a', 'b', 'c', 'a', 'a']
lista3 = [10, 20, 30, 40, 10, 10]

print("O elemento 2 aparece na lista1:", contar_elementos(lista1, 2))  
print("O elemento 'a' aparece na lista2:", contar_elementos(lista2, 'a'))  
print("O elemento 10 aparece na lista3:", contar_elementos(lista3, 10))  
print("O elemento 5 aparece na lista1:", contar_elementos(lista1, 5))  