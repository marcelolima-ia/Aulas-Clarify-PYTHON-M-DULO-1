nome = input ("Qual o seu nome?\n")
horario = int(input("Que horas são?\n"))
repeticoes = int(input("Quantas vezes deseja executar?\n"))

if horario <= 12:
    saudacao = "Bom dia"
elif horario <= 18:
    saudacao = "Boa tarde"
else:
    saudacao = "Boa noite"

def montarFrase(txt1,txt2):
    frase = f"{txt1} {txt2}, be happy"
    print(frase)

ligar = True
contador = 0
while ligar:
    montarFrase(saudacao,nome)
    contador = contador + repeticoes
    if contador >= repeticoes:
        ligar = False 