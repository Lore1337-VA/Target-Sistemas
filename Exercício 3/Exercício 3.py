import json

with open("C:\\Users\\S7ven\\OneDrive\\Desktop\\Entrevista\\Exercício 3\\dados.json", "r") as f:
    dados = json.load(f)

menorValor = 100000000
maiorValor = 0
acimaMedia = 0
valorTotal = float(0)
numeroDias = len(dados)

for i in range(numeroDias) :
    valorTotal = valorTotal + dados[i]["valor"]

media = float(valorTotal / numeroDias)

for i in dados :
    dia = i["dia"]
    valor = i["valor"]
    if valor < menorValor:
        if valor != 0 :
          menorValor = valor
    if valor > maiorValor:
        if valor != 0 :
          maiorValor = valor
    if valor > media:
        acimaMedia += 1

print("Menor faturamento:", menorValor)
print("Maior faturamento:", maiorValor)
print("Dias onde o faturamento foi acima da média:", acimaMedia)