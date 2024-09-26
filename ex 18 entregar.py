tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

tabuleiro[1][1] = "X"

for linha in tabuleiro:
    print("|".join(linha))