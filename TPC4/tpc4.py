
import json
import re

# 
def csv_to_json(csv_file, json_file):
    with open(csv_file, "r", encoding="utf-8") as f:
        dataset = f.readlines()

    data = []
    with open(json_file, "w", encoding="utf-8") as f:
        campos_cabecalho = re.split(r',(?!\d+})', dataset[0].strip())

        if len(campos_cabecalho) > 3:
            interv = re.findall(r'\d+,?\d*', campos_cabecalho[3])
            intervalos = interv[0].split(',')
            if len(intervalos) > 1:
                limite_inf = int(intervalos[0]) 
                limite_sup = int(intervalos[1])
            elif len(intervalos) == 1:
                limite_inf = 3
                limite_sup = int(intervalos[0])

            # Verifica se o campo tem uma função associada
            #funcao = re.search(r'\w+(?<=(::))', campo) 
            funcao = re.split(r'(::)', campos_cabecalho[3])
            if len(funcao) > 1:
                campos_cabecalho[3] = funcao[2]


        for line in dataset[1:]:
            dados = line.strip().split(',')
            registo = {}
            index = 0
            if len(campos_cabecalho) > 3:
                numeros = [int(num) for num in dados[limite_inf:limite_inf + limite_sup] if num != '']
            for campo in campos_cabecalho:
                if index < len(campos_cabecalho) - 1:
                    if index == 3:
                        if campo == "sum":
                            if campo not in registo.keys():
                                registo[campo] = sum(numeros)
                                index = limite_inf + limite_sup
                        elif campo == "media":
                            if campo not in registo.keys():
                                registo[campo] = sum(numeros) / len(numeros)
                                index = limite_inf + limite_sup
                        else:
                            registo["Notas"] = numeros
                    else:
                        registo[campo] = dados[index]
                        index += 1
            data.append(registo)

        print(data)

        #
        #json_str = json.dumps(data, ensure_ascii=False)
        #f.write(json_str)

csv_to_json("TPC4/alunos.csv", "TPC4/alunos.json")