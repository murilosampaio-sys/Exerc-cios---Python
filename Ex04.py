contador_par = 0
contador_impar = 0
contador = 0

for i in range(1,11):
    numero = int(input(f"Escreva seu {i} número: "))

    if numero % 2 == 0:
        contador_par = contador_par + 1

    else:
        contador_impar = contador_impar + 1

print(f"Você adicionou {contador_par} numeros pares e {contador_impar} numeros impares.")