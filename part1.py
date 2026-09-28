import csv
import statistics

# Caso for utilizar via .csv, mover o arquivo para a raiz do projeto com o nome 'dados.csv'

def choice_options():
    data = []
    try:
        with open('dados.csv', 'r', encoding='utf-8') as archive:
            if archive:
                lines = csv.reader(archive)
                for l in lines:
                    for item in l:  # Percorre cada elemento dentro da linha do CSV
                        data.append(int(item))
    except FileNotFoundError:
        numbers = input("Insira os números separados por ',' (ex: 1,2,3): ")
        numbers_list = numbers.split(',')
        for number in numbers_list:
            data.append(int(number))
    return data

def calculate():
    data = choice_options()
    mode = statistics.mode(data)
    mean = statistics.mean(data)
    median = statistics.median(data)
    print(f"Moda: {mode} | Média: {mean} | Mediana: {median}")

calculate()