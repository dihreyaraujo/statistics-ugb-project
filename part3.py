import math

dados = []

while len(dados) != 12:
    valor = int(input("Digite um valor: "))
    dados.append(valor)

dados.sort()

n = len(dados)

k = math.ceil(1 + 3.322 * math.log10(n))

h = (dados[-1] - dados[0]) / k
h = math.ceil(h)

# -----------------------------------------
# CRIA AS CLASSES AUTOMATICAMENTE
# -----------------------------------------

classes = []

limite = dados[0]

for i in range(k):

    lim_inf = limite
    lim_sup = lim_inf + h

    if i == k - 1:
        fi = sum(1 for x in dados if lim_inf <= x <= lim_sup)
    else:
        fi = sum(1 for x in dados if lim_inf <= x < lim_sup)

    classes.append((lim_inf, lim_sup, fi))

    limite = lim_sup

# -----------------------------------------
# TABELA
# -----------------------------------------

print("--------------------------------------------")
print(f"Total de dados (n): {n}")
print(f"Número de classes (k): {k}")
print(f"Amplitude da classe (h): {h}")

print("--------------------------------------------")
print("\nDISTRIBUIÇÃO DE FREQUÊNCIA")
print("\nClasse | fi | FI")

FI = 0

for lim_inf, lim_sup, fi in classes:
    FI += fi
    print(f"{lim_inf} - {lim_sup} | {fi} | {FI}")

# -----------------------------------------
# ENCONTRAR CLASSE
# -----------------------------------------

def encontrar_classe(posicao):

    FI = 0

    for lim_inf, lim_sup, fi in classes:

        FI_anterior = FI
        FI += fi

        if posicao <= FI:
            return lim_inf, fi, FI_anterior


# -----------------------------------------
# MODA
# -----------------------------------------

def moda():

    maior = 0
    xi = 0
    for lim_inf, lim_sup, fi in classes:

        if(fi > maior):
            maior = fi
            xi = (lim_inf + lim_sup) / 2

    print(f"Moda: {xi:.2f}")



# -----------------------------------------
# MÉDIA
# -----------------------------------------

def media():

    soma = 0

    for lim_inf, lim_sup, fi in classes:

        xi = (lim_inf + lim_sup) / 2

        soma += xi * fi

    print(f"Média: {soma / n:.2f}")

# -----------------------------------------
# MEDIANA
# 

def mediana():

    posicao = n / 2

    linf, fnd, fant = encontrar_classe(posicao)

    valor = linf + ((posicao - fant) / fnd) * h

    print(f"Mediana: {valor:.2f}")


# -----------------------------------------
# QUARTIL
# -----------------------------------------

def quartil(q):

    posicao = q * n / 4

    linf, fq, fant = encontrar_classe(posicao)

    valor = linf + ((posicao - fant) / fq) * h

    print(f"Q{q}: {valor:.2f}")


# -----------------------------------------
# DECIL
# -----------------------------------------

def decil(d):

    posicao = d * n / 10

    linf, fd, fant = encontrar_classe(posicao)

    valor = linf + ((posicao - fant) / fd) * h

    print(f"D{d}: {valor:.2f}")


# -----------------------------------------
# PERCENTIL
# -----------------------------------------

def percentil(p):

    posicao = p * n / 100

    linf, fp, fant = encontrar_classe(posicao)

    valor = linf + ((posicao - fant) / fp) * h

    return valor


# -----------------------------------------
# RESULTADOS
# -----------------------------------------
print("\n--------------------------------------------")
print("Medidas de posição")

moda()

media()

mediana()

quartil(1)
quartil(3)

decil(2)
decil(7)

print(f"P15: {percentil(15):.2f}")
print(f"P22: {percentil(22):.2f}")
print(f"P63: {percentil(63):.2f}")
print(f"P70: {percentil(70):.2f}")