import re

# a) Calcula a frequência de processos por ano
def processos():
    freq_processos = {}

    with open("TPC3/processos.txt" , "r") as f:
        for line in f.readlines():
            dados = line[:-1].split('::')
            if len(dados) > 1:
                data = dados[1].split('-')
                ano = data[0]

                total = len(re.findall(r'Proc.', line))
                if ano not in freq_processos.keys():
                    freq_processos[ano] = 0
                freq_processos[ano] += total

    for k,v in freq_processos.items():
        print(f"Ano: {k}                 Processos: {v}")


# b) Calcula a frequência de nomes próprios e apelidos por séculos e apresenta os 5 mais usados
def nomes():
    print("A")