import json
import re

# Função que converte um ficheiro .csv num ficheiro .json
def csv_to_json(csv_file, json_file):
    data = []

    # Lê o ficheiro de input
    with open(csv_file, "r", encoding="utf-8") as f:
        dataset = f.readlines()

    # Abre o ficheiro de output
    with open(json_file, "w", encoding="utf-8") as f:
        # Guarda os campos do cabeçalho
        campos_cabecalho = re.split(r',(?!\d+})', dataset[0].strip())
        
        # Percorre o dataset
        for line in dataset[1:]:
            dados = line.strip().split(',')
            registo = {}
            
            for index, campo in enumerate(campos_cabecalho):
                if campo != '':
                    # Verifica se o campo tem um intervalo associado
                    intervalo = re.search(r'{(\d+),?(\d+)?}', campo)
                    if intervalo:
                        if intervalo.group(2):
                            limite_inf = int(intervalo.group(1))
                            limite_sup = int(intervalo.group(2))
                        else:
                            limite_inf = limite_sup = int(intervalo.group(1))

                    # Verifica se o campo tem uma função associada
                    funcao = re.search(r'(?<=(::))\w+', campo) 
                    if funcao:
                        # Atualiza o campo para o nome da função 
                        campo = funcao.group(0)
                    
                    # Guarda os números numa lista, caso existam
                    if intervalo:
                        lista = [int(num) for num in dados[index:index + limite_sup] if num != '']
                        if len(lista) < limite_inf:
                            print("Número incorreto de dados no dataset")
                            break

                        # Verifica se o campo é uma das funções disponíveis; se não for associa ao campo a lista
                        if campo == "sum":
                            registo[campo] = sum(lista)
                        elif campo == "media":
                            registo[campo] = sum(lista) / len(lista)
                        else:
                            registo[campo.split('{')[0]] = lista
                    # Se não existir guarda apenas a única informação presente 
                    else:
                        registo[campo] = dados[index]

            # Armazena o dicionário registo numa lista
            data.append(registo)

        # Escreve no ficheiro .json
        json_str = json.dumps(data, ensure_ascii=False)
        f.write(json_str)

csv_to_json("TPC4/csv/alunos5.csv", "TPC4/json/alunos5.json")