numeros_pares = 0
contador_par = 0

for i in range(1,6):
    numero = int(input(f"Escreva seu {i} número: "))

    if numero % 2 == 0:
        contador_par = contador_par + 1
        numeros_pares = numeros_pares + numero

if contador_par == 0 :
    print("Você não botou nenhum número par.")

elif contador_par >= 1:
    media = numeros_pares / contador_par
    print(f"A média dos números somados foi: {media}")