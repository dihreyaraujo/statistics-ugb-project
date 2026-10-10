# statistics-ugb-project

Curso: Engenharia de Software
Disciplina: Probabilidade e Estatística
Professor: Marcelo Arantes

# Integrantes:
- Dihrey
- Cauã Barbosa Salomão (2026101137)
- Artur
- Yuri Barbosa
- Pablo Ferreira Sampaio (2026101868)



# Introdução

O programa dividido em três partes serve como um motor de análise estatística descritiva, onde o usuário fornece dados brutos e o programa entrega os resultados já processados e calculados.



# Arquitetura

O projeto é composto por três scripts independentes, um para cada parte do trabalho:

part1.py: lê os dados (arquivo dados.csv ou digitação) e calcula moda, média e mediana com o pacote "statistics".

part2.py: transforma os dados em uma tabela de frequências (valor, frequência absoluta e frequência acumulada) e calcula as medidas a partir dela.

part3.py: agrupa os dados em classes (Fórmula de Sturges) e calcula as medidas de tendência central e as separatrizes por interpolação, sem bibliotecas estatísticas.



# Execução

Requisitos: Python 3.8 ou superior. Não é necessário instalar bibliotecas externas.

python part1.py
python part2.py
python part3.py

Partes 1 e 2: digite os números separados por vírgula (ex.: 1,2,3). Na Parte 1, também é possível colocar um arquivo "dados.csv" na pasta do projeto, com os números separados por vírgula.
Parte 3: o programa pede 12 valores, um por vez.



# PARTE 1

A primeira parte do programa serve para calcular as Medidas de Tendência Central de um conjunto de dados não agrupados, utilizando o pacote nativo "statistics" do Python solicitado no documento do trabalho.

A função "choice_options" serve para caso o usuário tiver um arquivo .csv já com os dados que ele precisa calcular, onde o programa identifica se teria entrada de arquivos .csv ou não. Caso não localizar um arquivo .csv, ele pede ao usuário para fornecer os dados manualmente no terminal.

Ao receber os dados, o programa passa por "calculate", que processa os dados em Moda, Média e Mediana e entrega ao usuário no final do programa.

Exemplo:
Insira os números separados por ',' (ex: 1,2,3):

1,5,7,4,8,3,8,9,1,3,8,6,3,4,4,8,9,7,6   # Entrada dos dados

Moda: 8 | Média: 5.473684210526316 | Mediana: 6   # Saída



# PARTE 2

Para essa parte do programa, calculamos um conjunto de dados agrupados sem intervalo de classe, com uma tabela de fácil leitura para o usuário.

O usuário insere os dados para o programa e ele identifica a frequência com "identify_frequency", processando os dados e guardando na lista "result". Em "print_table", o programa imprime a parte de frequência da tabela, classificando em Valor (Xi), Freq. Absoluta (fi) e Freq. Acumulada (Fi).

"calculate_median" passa por uma estrutura condicional "if" para identificar se o total de elementos é par ou ímpar, onde irá escolher duas formas de calcular a mediana dos dados fornecidos.
"execute" passa pelos cálculos de Moda, Média e Mediana e imprime as Estatísticas abaixo da Tabela de Frequência.

A média é calculada por Σ(xi · fi) / n. A moda é o valor (ou valores) de maior frequência absoluta. A mediana usa a frequência acumulada: se n é ímpar, é o primeiro valor cuja frequência acumulada alcança a posição (n+1)/2; se n é par, é a média dos valores nas posições n/2 e n/2 + 1.

Exemplo:

Insira os números separados por ',' (ex: 1,2,3): 1,5,7,4,8,3,8,9,1,3,8,6,3,4,4,8,9,7,6

Valor (Xi)  |  Freq. Absoluta (fi)  |  Freq. Acumulada (Fi)
-------------------------------------------------------
     1      |          2           |         2
     3      |          3           |         5
     4      |          3           |         8
     5      |          1           |         9
     6      |          2           |         11
     7      |          2           |         13
     8      |          4           |         17
     9      |          2           |         19
--- Estatísticas ---
Média: 5.47 | Moda: [8] | Mediana: 6



# PARTE 3

Nessa parte do programa o arquivo do trabalho fornecido pelo professor proíbe o uso de qualquer biblioteca estatística ou análise de dados, fazendo com que o programador utilize o próprio conhecimento que aprendeu nas aulas até agora para completar o programa.
 
O foco dessa parte do programa para processar e calcular é: Quantidade de Classes; Intervalo de Classe; Freq. Absoluta; Frequência Acumulada; Medidas de Tendência Central; e Medidas de Posição (Separatrizes).

O usuário digita os valores, que são ordenados e guardados em "dados". Com o total de elementos "n", o programa calcula a quantidade de classes "k" pela Fórmula de Sturges (k = 1 + 3,322 . log10(n)), e a amplitude do intervalo "h" = (maior valor - menor valor) / k. Os dois valores resultantes são arredondados para cima com "math.ceil".

Em seguida, o programa cria as classes automaticamente. A primeira classe começa no menor valor e cada classe seguinte começa onde a anterior termina, somando "h" ao limite inferior. Os intervalos são fechados à esquerda e abertos à direita, exceto o último, que é fechado nos dois lados para que o maior valor não fique de fora. A frequência absoluta (fi) é a quantidade de dados dentro de cada classe, e a frequência acumulada (FI) é a soma progressiva das frequências. Tudo isso é impresso na tabela de distribuição de frequência.

"encontrar_classe" recebe uma posição e descobre em qual classe ela está, acumulando as frequências até encontrar a primeira classe em que a posição é menor ou igual à frequência acumulada. A função devolve o limite inferior da classe, a frequência absoluta dela e a frequência acumulada da classe anterior, que são os valores necessários para as fórmulas de interpolação.

"moda" encontra a classe de maior frequência absoluta e retorna o ponto médio dela, (limite inferior + limite superior) / 2. "media" calcula o ponto médio (xi) de cada classe, soma xi · fi e divide por "n".

"mediana", "quartil", "decil" e "percentil" usam a mesma fórmula de interpolação linear:
valor = Linf + ((posição - F anterior) / f) · h
O que muda é a posição: n/2 para a mediana, q·n/4 para o quartil, d·n/10 para o decil e p·n/100 para o percentil. Linf é o limite inferior da classe encontrada, F anterior é a frequência acumulada da classe anterior, f é a frequência absoluta da classe e h é a amplitude.

Exemplo:

Digite um valor: 1
Digite um valor: 5
Digite um valor: 7
Digite um valor: 4
Digite um valor: 8
Digite um valor: 3
Digite um valor: 8
Digite um valor: 9
Digite um valor: 1
Digite um valor: 3
Digite um valor: 8
Digite um valor: 6
--------------------------------------------
Total de dados (n): 12
Número de classes (k): 5
Amplitude da classe (h): 2
--------------------------------------------

DISTRIBUIÇÃO DE FREQUÊNCIA

Classe | fi | FI
1 - 3 | 2 | 2
3 - 5 | 3 | 5
5 - 7 | 2 | 7
7 - 9 | 4 | 11
9 - 11 | 1 | 12

--------------------------------------------
Medidas de posição
Moda: 8.00
Mediana: 6.00
Q3: 8.00
D7: 7.70
P15: 2.80
P22: 3.43
P63: 7.28
P70: 7.70
