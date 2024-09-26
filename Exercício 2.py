numAnt1 = 0
numAnt2 = 1
numAtual = 0
controle = 0

numeroInserido = int(input("Insira um número: "))

while controle < numeroInserido :
  numAtual = numAnt1 + numAnt2
  numAnt1 = numAnt2
  numAnt2 = numAtual
  controle = controle + 1
  if numAtual == numeroInserido :
    print(f"O número {numeroInserido} está na sequência de Fibonacci")
    break

if numAtual != numeroInserido :
  print(f"O número {numeroInserido} não está na sequência de Fibonacci")