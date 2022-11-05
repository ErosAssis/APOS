vet = [0.0]*3

for cont in range(0, 3, 1):
    vet[cont] = float(input("Informe o número: "))
    if (vet[cont] % 2 == 0):
        vet[cont] = vet[cont] * 1.02
    else:
        vet[cont] = vet[cont] * 1.05

for cont in range(0, 3, 1):
    print(vet[cont])
