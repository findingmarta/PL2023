from time import sleep
import json
import re
import os

# Init
f = open("TPC3/processos.txt" , "r")
dataset = f.readlines()


# a) Calcula a frequência de processos por ano
def processos():
    texto = ''.join(dataset)

    print("\n{:<10} NÚMERO DE PROCESSOS\n".format('ANO'))
    for ano in range(1600,2050):
        n_processos = len(re.findall(rf"::{ano}-", texto))
        if n_processos > 0:
            print("{:<10}".format(ano) + str(n_processos))


# b) Calcula a frequência de nomes próprios e apelidos por séculos e apresenta os 5 mais usados
def nomes(seculo, opcao):      
    match_sec = []  
    freq_proprios = {}
    freq_apelidos = {}

    # Procurar as entradas que correspondem a um determinado século
    for line in dataset:
        if (re.search(rf"::{seculo-1}[0-9][0-9]-", line)):
            match_sec.append(line)

    # Determinar a frequência de nomes para cada entrada de um determinado século
    for line in match_sec:
        dados = re.split(r'::', line[:-1])
        if len(dados) > 1:
            nome = re.split(r' ', dados[2])

            # Armazena os nomes próprios
            if opcao == 1:
                if nome[0] not in freq_proprios.keys():
                    freq_proprios[nome[0]] = 1
                else:
                    freq_proprios[nome[0]] += 1

            # Armazena os apelidos
            elif opcao == 2:
                if nome[len(nome) - 1] not in freq_apelidos.keys():
                    freq_apelidos[nome[len(nome) - 1]] = 1
                else:
                    freq_apelidos[nome[len(nome) - 1]] += 1

    if opcao == 1:
        # Ordenar o dicionário
        sorted_proprios = sorted(freq_proprios.items(), key=lambda x:x[1], reverse=True)
        converted_proprios = dict(sorted_proprios)

        # Imprimir as frequências 
        print("\n{:<20}FREQUÊNCIA\n".format('NOME PRÓPRIO'))
        for k,v in converted_proprios.items():
            print("{:<20}".format(k) + str(v))

        # Imprimir o TOP 5
        print(f"\n ---------- TOP 5 Nomes Próprios No Século {seculo} ---------- \n")
        for index in range(0,5):
            nome = sorted_proprios[index][0]
            frequencia = sorted_proprios[index][1]
            print("{:<20}".format(nome) + str(frequencia))

    elif opcao == 2:
        # Ordenar o dicionário
        sorted_apelidos = sorted(freq_apelidos.items(), key=lambda x:x[1], reverse=True)
        converted_apelidos = dict(sorted_apelidos)   

        # Imprimir as frequências 
        print("\n{:<20}FREQUÊNCIA\n".format('APELIDO'))
        for k,v in converted_apelidos.items():
            print("{:<20}".format(k) + str(v))

        # Imprimir o TOP 5
        print(f"\n ---------- TOP 5 Apelidos No Século {seculo} ---------- \n")
        for index in range(0,5):
            nome = sorted_apelidos[index][0]
            frequencia = sorted_apelidos[index][1]
            print("{:<20}".format(nome) + str(frequencia))


# c) Calcula a frequência dos vários tipos de relação: irmão, sobrinho, etc.
def relacoes():
    freq_relacoes = {}
    relacoes_validas = ["avo", "avos", "mae", "pai", "pais", "irmao", "irmaos", "tio", "tios", "neto", "netos", "filho", "filhos", "bisavo", "bisavos", "primo", "primos", "sobrinho", "sobrinhos"]
    
    for line in dataset:
        dados = re.split(r'::', line[:-1])
        extra = dados[len(dados) - 2]
        
        relacoes = re.findall(r',[aA-zZ]*[ ]*[aA-zZ]*\.', extra)
        
        for relacao in relacoes:
            if relacao[1:-1] not in freq_relacoes.keys(): 
                aux = relacao[1:-1].split(' ')
                if aux[0].lower() in relacoes_validas:
                    freq_relacoes[relacao[1:-1]] = 1
            else:
                freq_relacoes[relacao[1:-1]] += 1

    # Imprime a frequência de cada relação encontrada
    print("\n{:<20}FREQUÊNCIA\n".format('RELAÇÃO'))
    for k, v in freq_relacoes.items():
        print ("{:<20}".format(k) + str(v))


# d) Converta os 20 primeiros registos num novo ficheiro de output mas em formato Json.
def convert_to_json():
    data = []
    
    print("A converter para JSON...\n")
    for index in range(0,20):
        dados = dataset[index].strip().split("\n")
        registo = {}
        for index, campo in enumerate(dados):
            key = 'processo'.format(index+1)
            registo[key] = campo
        data.append(registo)

    json_str = json.dumps(data)
    print("A escever no novo ficheiro...\n")
    with open("TPC3/processos.json", "w", encoding="utf-8") as f:
        f.write(json_str)
    print("Conlcuido!\n")


# Menu secundário destinado à alinea b)
def menu_nomes():
    os.system('cls')
    print("1 - Frequência de nomes próprios por século")
    print("2 - Frequência de apelidos por século")
    print("0 - Sair")
    print("\n")
    opcao = int(input("Qual a sua opção? "))
    print("\n")

    if opcao == 0:
        print("Saindo...")
        return
    elif opcao in [1,2]:
        os.system('cls')
        print("17 - Século 17")
        print("18 - Século 18")
        print("19 - Século 19")
        print("20 - Século 20")
        print("0 - Voltar")
        print("\n")
        seculo = int(input("Selecione o século: "))
        print("\n")
        
        if seculo == 0:
            menu_nomes()
        elif seculo in [17,18,19,20]:
            nomes(seculo, opcao)
        else:
            print("Século inválido")
            sleep(1)
            menu_nomes()
    else:
        print("Opção inválida")
        sleep(1)
        menu_nomes()


# Menu Principal
def menu():   
    os.system('cls')
    print("1 - Frequência de processos por ano")
    print("2 - Frequência de nomes próprios e de apelidos por século")
    print("3 - Frequência de tipos de relação")
    print("4 - Converter para JSON")
    print("0 - Sair")
    print("\n")
    opcao = int(input("Qual a sua opção? "))
    print("\n")

    if opcao == 1:
        processos()
    elif opcao == 2:
        menu_nomes()
    elif opcao == 3:
        relacoes()
    elif opcao == 4:
        convert_to_json()
    elif opcao == 0:
        print("Saindo...")
    else:
        print("Opção inválida!")
        sleep(1)
        menu()  
    
menu()