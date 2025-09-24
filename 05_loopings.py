palavra = "tamgamandapio"
contador = 0

#PARA CADA(FOR) LETRA NA(IN) PALAVRA

for letra in palavra:
    contador = contador + 1
    print(f"{contador} - {letra}")
    #print("\n")


cidades = [
    'Fortaleza',
    'Belem',
    'Recife',
    'Poa',
    'Sao Paulo'
]

#print(cidades[0])

for cidade in cidades:
    print(cidade)

#-------------------------------------

botaoExecutar = True

contador02 = 0

while botaoExecutar:
    print(contador02)
    contador02 = contador02 + 1
    if contador02 >= 200:
        botaoExecutar = False