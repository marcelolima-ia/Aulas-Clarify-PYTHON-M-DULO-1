

nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite o ano em que você nasceu: "))

ano_atual = 2025
idade = ano_atual - ano_nascimento
print(f"{nome}, você tem {idade} anos.")

contador = 0
repetir = input("Deseja fazer de novo?\n [1] Sim\n [2] Não\n")



'''def chama():
    nome = input("Digite seu nome: ")
    ano_nascimento = int(input("Digite o ano em que você nasceu: "))

    ano_atual = 2025
    idade = ano_atual - ano_nascimento
    print(f"{nome}, você tem {idade} anos.")


    repetir = input("Deseja fazer de novo?\n [1] Sim\n [2] Não\n")
    if repetir != '1':
        print("Encerrando o programa.")
    else:
        chama()

chama()'''

while True:
    nome = input("Digite seu nome: ")
    ano_nascimento = int(input("Digite o ano em que você nasceu: "))

    ano_atual = 2025
    idade = ano_atual - ano_nascimento

    print(f"{nome}, você tem {idade} anos.")

    repetir = input("Deseja fazer de novo?\n [1] Sim\n [2] Não\n")
    if repetir != '1':
        print("Encerrando o programa.")
        break
 
#https://servicodados.ibge.gov.br/api/v2/censos/nomes/marcelo
#https://servicodados.ibge.gov.br/api/docs/