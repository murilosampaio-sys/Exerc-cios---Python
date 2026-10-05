nomes = []
idades = []

idade_mais_velha = 0
posicao_idade = 0

for i in range(1, 6):
    nome = input("Escreva seu nome: ")
    idade = int(input("Escreva sua idade em anos: "))

    nomes.append(nome)
    idades.append(idade)

for i in range(len(idades)):
    if idades[i] > idade_mais_velha:
        idade_mais_velha = idades[i]
        posicao_idade = i

print(f"A pessoa mais velha é - Nome: {nomes[posicao_idade]}, idade = {idade_mais_velha}")