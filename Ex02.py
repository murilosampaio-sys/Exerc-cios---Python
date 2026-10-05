ano_atual = 2026

ano_nascimento = int(input("Escreva o ano que você nasceu: "))

idade = ano_atual - ano_nascimento

if idade >= 18:
    print("VcoÊ já é de maior e pode fazer a carteira de motorista. ")

elif idade < 18 and idade >= 16:
    print("Você já pode votar.")