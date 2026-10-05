numeros_somados = 0 
for i in range(1,11):
    numero_soma = int(input(f"Escreva seu {i} número para somar aos outros: "))
    numeros_somados = numeros_somados + numero_soma

print(f"A somas dos números adicionados foi {numeros_somados}")
