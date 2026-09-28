from collections import Counter

def insert_numbers():
    numbers = input("Insira os números separados por ',' (ex: 1,2,3): ")
    return [int(number.strip()) for number in numbers.split(',')]

def identify_frequency(data):
    total_count = Counter(data)
    
    result = []
    acumulada = 0
    for number in sorted(total_count.keys()):
        qtd = total_count[number]
        acumulada += qtd
        result.append({
            "value": number,
            "count": qtd,
            "accumulated": acumulada
        })
    return result

def print_table(data):
    print("\nValor (Xi)  |  Freq. Absoluta (fi)  |  Freq. Acumulada (Fi)")
    print("-" * 55)
    for vf in data:
        print(f"     {vf['value']:<6} |          {vf['count']:<11} |         {vf['accumulated']}")

def calculate_median(data_obj, total_elements):
    if total_elements % 2 != 0:
        posicao = (total_elements + 1) / 2
        for vf in data_obj:
            if vf['accumulated'] >= posicao:
                return vf['value']
                
    else:
        pos1 = total_elements / 2
        pos2 = (total_elements / 2) + 1
        
        val1, val2 = None, None
        for vf in data_obj:
            if val1 is None and vf['accumulated'] >= pos1:
                val1 = vf['value']
            if val2 is None and vf['accumulated'] >= pos2:
                val2 = vf['value']
        
        return (val1 + val2) / 2

def execute():
    data = insert_numbers()
    data_obj = identify_frequency(data)
    print_table(data_obj)
    
    N = len(data) 
    
    meanSum = sum([vf['value'] * vf['count'] for vf in data_obj])
    mean = meanSum / N
    
    max_count = max(vf['count'] for vf in data_obj)
    mode = [vf['value'] for vf in data_obj if vf['count'] == max_count]
    
    median = calculate_median(data_obj, N)

    print("--- Estatísticas ---")
    print(f"Média: {mean:.2f} | Moda: {mode} | Mediana: {median}")

execute()
