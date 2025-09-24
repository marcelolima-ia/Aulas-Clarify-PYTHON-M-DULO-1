
import json, requests


pedir = input
resposta = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/marcelo")

dados = json.loads(resposta.text)
print(dados[0]['res'][2])





#https://colab.research.google.com/
#https://app.inventor.mit.edu/