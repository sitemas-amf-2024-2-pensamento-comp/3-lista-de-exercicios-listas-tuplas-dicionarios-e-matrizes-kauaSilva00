pontos = (100, 200, 300)

try:
    pontos[0] = 150 
except TypeError as e:
    print(f"Erro: {e}") 
