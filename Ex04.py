contador_par = 0
contador_impar = 0
numeros_pares = 0
numeros_impares = 0

for i in range(1, 11):
    numero = int(input(f"Escreva seu {i}º número: "))

    if numero % 2 == 0:
        contador_par = contador_par + 1
        numeros_pares = numeros_pares + numero
    else:
        contador_impar = contador_impar + 1
        numeros_impares = numeros_impares + numero

print(f"\nVocê adicionou {contador_par} números pares e {contador_impar} números ímpares.")
print(f"A soma de todos os números pares é {numeros_pares} e a soma de todos os números ímpares é {numeros_impares}.")