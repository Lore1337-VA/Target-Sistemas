SP = float(67836.43)
RJ = float(36678.66)
MG = float(29229.88)
ES = float(27165.48)
Outros = float(19849.53)

valorTotal = SP + RJ + MG + ES + Outros

porcSP = SP / valorTotal * 100
porcRJ = RJ / valorTotal * 100
porcMG = MG / valorTotal * 100
porcES = ES / valorTotal * 100
porcOutros = Outros / valorTotal * 100

print ("Porcentagem de SP: %.2f" %porcSP)
print ("Porcentagem de RJ: %.2f" %porcRJ)
print ("Porcentagem de MG: %.2f" %porcMG)
print ("Porcentagem de ES: %.2f" %porcES)
print ("Porcentagem de Outros: %.2f" %porcOutros)