def fibonacci(n):

    sequencia = []
    
    for i in range(n):
        if i == 0:
            sequencia.append(0)
        elif i == 1:
            sequencia.append(1)  
        else:
            proximo = sequencia[-1] + sequencia[-2] 
            sequencia.append(proximo)

    return sequencia

print("Fibonacci (n=5):", fibonacci(5))   
print("Fibonacci (n=10):", fibonacci(10)) 
print("Fibonacci (n=0):", fibonacci(0))    