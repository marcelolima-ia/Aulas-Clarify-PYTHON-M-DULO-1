estados = ['SP', 'CE','PA', 'PE']
contador = 0
def regioes (informacao, valor):
    print(f"{valor} - {informacao}")

for estado in estados:
    contador += 1
    regioes(estado,contador)