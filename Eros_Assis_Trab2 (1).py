matriz = [[0]*3, [0]*3, [0]*3,[0]*3, [0]*3, [0]*3,[0]*3, [0]*3, [0]*3,[0]*3,[0]*3, [0]*3, [0]*3,[0]*3, [0]*3, [0]*3,[0]*3, [0]*3, [0]*3,[0]*3,[0]*3, [0]*3, [0]*3,[0]*3, [0]*3, [0]*3,[0]*3, [0]*3, [0]*3,[0]*3,[0]*3, [0]*3, [0]*3,[0]*3, [0]*3, [0]*3,[0]*3, [0]*3, [0]*3,[0]*3]
matriz2 = [[0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5, [0.0]*5]
linha = 0
coluna = 0
escolha = 0
ra = 0
cpf = 0
codigo = 0
nota = 1
media = 0.0
contador = 0
escolha2 = " "
invalido = 0
continuar = 0


for linha in range(0,40,1):
    for coluna in range(0,1,1):
      matriz[linha][coluna]= int(input("Informe o número do RA do aluno " + str(linha + 1) +": " ))

    for coluna in range(1,2,1):
        matriz[linha][coluna]= int(input("Informe o número do CPF do aluno " + str(linha + 1) +": " ))

    for coluna in range(2,3,1):
        matriz[linha][coluna]= int(input("Informe o número do Código do aluno " + str(linha + 1) +": " ))
        matriz2[linha][4] = matriz[linha][coluna]
        print()
    
for linha in range(0,40,1):
    for coluna in range(0,4,1):
        matriz2[linha][coluna]= int(input(f"Informe a nota {nota} do aluno " + str(linha + 1) +": " ))
        nota = nota + 1
        if nota == 5:
            nota = 1
    print()

while continuar == 0:  
 escolha = int(input("Informe o tipo de consulta: | (1-RA, 2-CPF e 3-Código) |"))

    
 if escolha == 1:
        ra = int(input("Informe o RA: "))
        for linha in range(0,40,1):
     
            if ra == matriz[linha][0]:
                print(f"As notas do RA {ra} é: {matriz2[linha][0]} {matriz2[linha][1]} {matriz2[linha][2]} {matriz2[linha][3]}") 
                media = (matriz2[linha][0] + matriz2[linha][1] + matriz2[linha][2] + matriz2[linha][3]) / 4 
                invalido = 1
                print(f"A média é {media} ")  
                if media >= 6:
                    print("Aluno Aprovado")
                elif media < 6 and media >= 4:
                    print("Aluno de Recuperação")
                else:
                    print("Aluno Reprovado")

        if invalido == 0:
         print("Código Inválido")



 elif escolha == 2:
        cpf = int(input("Informe CPF: "))
        for linha in range(0,40,1):
     
            if cpf == matriz[linha][1]:
                print(f"As notas do CPF {cpf} é: {matriz2[linha][0]} {matriz2[linha][1]} {matriz2[linha][2]} {matriz2[linha][3]}") 
                media = (matriz2[linha][0] + matriz2[linha][1] + matriz2[linha][2] + matriz2[linha][3]) / 4 
                invalido = 1
                print(f"A média é {media} ")  
                if media >= 6:
                    print("Aluno Aprovado")
                elif media < 6 and media >= 4:
                    print("Aluno de Recuperação")
                else:
                 print("Aluno Reprovado")
        
        if invalido == 0:
            print("Código Inválido")

 elif escolha == 3:
        codigo = int(input("Informe o Código: "))
        for linha in range(0,40,1):
     
            if codigo == matriz[linha][2]:
                print(f"As notas do Código {codigo} é: {matriz2[linha][0]} {matriz2[linha][1]} {matriz2[linha][2]} {matriz2[linha][3]}") 
                media = (matriz2[linha][0] + matriz2[linha][1] + matriz2[linha][2] + matriz2[linha][3]) / 4 
                invalido = 1
                print(f"A média é {media} ")  
                if media >= 6:
                    print("Aluno Aprovado")
                elif media < 6 and media >= 4:
                    print("Aluno de Recuperação")
                else:
                    print("Aluno Reprovado")

        if invalido == 0:
            print("Código Inválido")

 invalido = 0

 escolha2 = (input("Deseja fazer uma nova pesquisa?  -   S (SIM) para continuar ou N (NÃO) para finalizar."))
 if escolha2 == "S":
    continuar = 0
 else:
    continuar = 1
    print("Fim do programa")

