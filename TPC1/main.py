dados = []
sexos = {"M": [0,0], "F": [0,0]}
faixas_etarias = dict()
niveis_colesterol = dict()

def parseFile():
    # Guardamos a informação do ficheiro em memória
    with open("TPC1/myheart.csv", "r") as f:
        for line in f.readlines()[1:]:
            # [:-1] para ignorar o \n
            dados_pessoa = line[:-1].split(',') 
            dados.append(dados_pessoa)  

def set_sexos():
    for dado in dados:
        if dado[1] in ['M','F']:
            sexos[dado[1]][1] += 1
            if int(dado[5]) == 1:
                sexos[dado[1]][0] += 1  

# Devolve o minimo (pre definido) e o maximo da idade
def get_max_idade():
    min = 30
    max = 0
    for dado in dados:
        if int(dado[0]) > max:
            max = int(dado[0])
    return (min,max)

def set_faixas_etarias():
    # Procura o valor máximo da idade no dataset dado
    min, max = get_max_idade()

    # Define as faixas etárias
    while min <= max:
        faixas_etarias[min] = [0,0]
        min += 5
    
    # Define a quantidade de pessoas doentes para cada faixa de etária
    for dado in dados:
        for key in faixas_etarias.keys():
            if key <= int(dado[0]) <= key + 4:
                faixas_etarias[key][1] += 1
                if int(dado[5]) == 1:
                    faixas_etarias[key][0] += 1

# Devolve o valor minimo e máximo do colesterol no dataset dado
def get_min_max_colesterol():
    min = 100000
    max = 0
    for dado in dados:
        if int(dado[3]) < min:
            min = int(dado[3])
        if int(dado[3]) > max:
            max = int(dado[3])
    return (min,max)

def set_niveis_colesterol():
    # Procura o valor minimo e máximo do colesterol no dataset dado
    min, max = get_min_max_colesterol()

    # Define os niveis de colesterol
    while min <= max:
        niveis_colesterol[min] = [0,0]
        min += 11
    
    # Define a quantidade de pessoas doentes para cada nivel de colesterol
    for dado in dados:
        for key in niveis_colesterol.keys():
            if key <= int(dado[3]) <= key + 10:
                niveis_colesterol[key][1] += 1
                if int(dado[5]) == 1:
                    niveis_colesterol[key][0] += 1

# Imprime uma tabela segundo uma distribuicao
def tabela(opcao, distrbuicao):   
    for k, v in distrbuicao.items():
        if v[1] != 0:
            perc = v[0] / v[1] * 100
        else:
            perc = 0
        
        if opcao == 1:
            if k == 'M':
                s = "Masculino"
            else:
                s = "Feminino"
            print ("{:<15}".format(s) + str(round(perc,2)) + "%")
        elif opcao == 2:
            print ("{:<20}".format(str(k) + " - " + str(k+4) + " anos") + str(round(perc,2)) + "%")
        elif opcao == 3:
            print ("{:<20}".format(str(k) + " - " + str(k+10)) + str(round(perc,2)) + "%")

# Menu principal do programa  
def menu():
    # Fazemos o parse dos ficheiros
    parseFile()
    
    # Preenchemos os dicionários com a informação guardada
    set_sexos()
    set_faixas_etarias()
    set_niveis_colesterol()
    
    print("1 - Percentagem de doentes por sexo")
    print("2 - Percentagem de doentes por faixa etária")
    print("3 - Percentagem de doentes por nível de colesterol")
    print("0 - Sair")
    print("\n")
    opcao = input("Qual a sua opção? ")
    print("\n")
    if int(opcao) == 1:
        # Header da tabela
        print("{:<15}COM DOENÇA".format('SEXO'))
        tabela(int(opcao), sexos)
    elif int(opcao) == 2: 
        # Header da tabela
        print("{:<20}COM DOENÇA".format('FAIXA ETÁRIA'))
        tabela(int(opcao), faixas_etarias)
    elif int(opcao) == 3:
        # Header da tabela
        print("{:<20}COM DOENÇA".format('NÍVEL COLESTEROL'))         
        tabela(int(opcao), niveis_colesterol)
    elif int(opcao) == 0:
        print("Saindo...")
    else:
        print("Opção inválida!")
        menu()

menu()
