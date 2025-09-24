def MinhaFuncao():
    print("Bom dia Python")


MinhaFuncao()

contador = 0
ativar = True
while ativar:
    MinhaFuncao()
    contador = contador + 1
    if contador >= 10:
        ativar = False

print("terminei")