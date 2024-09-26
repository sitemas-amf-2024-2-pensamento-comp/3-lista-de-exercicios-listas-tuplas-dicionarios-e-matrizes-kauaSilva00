idades = []

while True:
    idade = int(input("Digite a idade (ou 0 para sair): "))
    if idade == 0:
        break
    idades.append(idade)

if len(idades) > 0:
    media_idades = sum(idades) / len(idades)
    print("A média das idades é:", media_idades)
else:
    print("Nenhuma idade foi digitada.")