

tipoEscola = input("Estuda em colegio: \n [1]Publico\n[2]Particular\n")
nomeAluno = input('Qual o nome do aluno? \n')
mediaAluno = int(input('Qual a média do aluno' + " " + nomeAluno + "? \n"))
freqAluno = int(input("Qual a frequencia do aluno " + nomeAluno + "?\n"))

'''
!= diferente
== Igual
<= menor ou igual
>= maior ou igual
< Menor
> Maior
'''
if tipoEscola == "2":
    print("--------------------------------Escola Particular ------------------------------------")
    if mediaAluno >= 7 and freqAluno >= 70:
        status = "Aprovado"
    else:
        status = 'Reprovado'

    
if tipoEscola == "1":
    ("-------------------------------- Escola Publica ------------------------------------")
    if mediaAluno >= 6 or freqAluno >= 70:
        status = "Aprovado"
    else:
        status = 'Reprovado'
    

print('O Aluno ' + nomeAluno + " foi " + str(status) + " com média " + str(mediaAluno))
print('O Aluno ' , nomeAluno , " foi " , status , " com média " , mediaAluno)
print(f'O Aluno {nomeAluno} foi {status} com média {mediaAluno}')