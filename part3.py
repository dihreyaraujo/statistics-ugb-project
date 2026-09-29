import math


dados = [18, 19, 21, 22, 24, 25, 26, 27, 29, 30, 31, 33]
dados.sort()

n = len(dados)

last = len(dados) -1 

k = math.ceil(1 + 3.322 * math.log10(n))

# h = AT / k
h = (dados[last] - dados[0] ) / k 

amplitude_classe = dados[2] - dados[0]

print('--------------------------------------------')


print(f"Total de dados (n): {n}")

print(f"Número de classes (k): {k}")

print(f"Amplitude Total (h): {h}")

print('--------------------------------------------')


print("\nDISTRIBUIÇÃO DE FREQUÊNCIA (COM INTERVALO)")

print("\nClasse | fi | FI")

print(f"\n{dados[0]} - {dados[2]} | 2  | 2") 
print("21 - 24 | 2  | 4")
print("24 - 27 | 3  | 7")
print("27 - 30 | 2  | 9")
print("30 - 33 | 3  | 12")


print(f"\nIntervalo de classe: {amplitude_classe}")


print("\n Calculados via Fórmulas de Interpolação:")

print('\n --------------------------------------------')

def media():
    classes_fi = [
        (18, 21), 
        (21, 24),
        (24, 27),
        (27, 30),
        (30, 33)
    ]

    soma_xi_fi = 0
   

    for lim_inf, lim_sup in classes_fi:
        xi = (lim_inf + lim_sup) / 2
        soma_xi_fi += xi

    mediaC = soma_xi_fi / n
    
    print(f"Media: {mediaC}")
media()

def moda():
    L_inf = 24
    f_ant = 2
    f_post = 2

    king =  L_inf + (f_post / f_ant + f_post) * h

    print(f"Moda (King): {king}")
moda()

def mediana():
    
    linf = 24
    fant = 4
    fnd = 3
    h_m = h 

    mediana = linf + (((n / 2) - fant) * h_m  ) / fnd

    print(f"Mediana: {mediana}")
mediana()

