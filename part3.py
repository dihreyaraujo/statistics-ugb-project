import math


dados = [18, 19, 21, 22, 24, 25, 26, 27, 29, 30, 31, 33]
dados.sort()

n = len(dados)

last = len(dados) -1 

k = math.ceil(1 + 3.322 * math.log10(n))

# h = AT / k
h = (dados[last] - dados[0] ) / k 

print('--------------------------------------------')


print(f"Total de dados (n): {n}")

print(f"Número de classes (k): {k}")

print(f"Amplitude Total (h): {h}")

print('--------------------------------------------')


print("\nDISTRIBUIÇÃO DE FREQUÊNCIA (COM INTERVALO)")

print("\nClasse | fi | FI")

print("\n18 - 21 | 2  | 2") 
print("21 - 24 | 2  | 4")
print("24 - 27 | 3  | 7")
print("27 - 30 | 2  | 9")
print("30 - 33 | 3  | 12")


print("Calculados via Fórmulas de Interpolação:")

print('\n --------------------------------------------')