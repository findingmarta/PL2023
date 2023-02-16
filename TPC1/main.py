
sexos = {"M": 0, "F": 0}
faixas_etarias = {"30-34" : 0, "35-39" : 0, "40-44" : 0, "45-49" : 0, "50-54" : 0, "55-59" : 0, "60-64" : 0, "65-69" : 0, "+70" : 0}
niveis_colesterol = dict()

def parseFile():
    with open("TPC1/myheart.csv", "r") as f:
        for line in f.readlines()[1:]:
            args = line.split(',')

            idade = int(args[0])            

            #
            if args[1] in ['M', 'F']:
                sexos[args[1]] += 1

            #
            if 30 <= idade <= 34:
                faixas_etarias["30-34"] += 1
            elif 30 <= idade <= 34:
                faixas_etarias["35-39"] += 1    
            elif 40 <= idade <= 44:
                faixas_etarias["40-44"] += 1
            elif 45 <= idade <= 49:
                faixas_etarias["45-49"] += 1
            elif 50 <= idade <= 54:
                faixas_etarias["50-54"] += 1
            elif 55 <= idade <= 59:
                faixas_etarias["55-59"] += 1
            elif 60 <= idade <= 64:
                faixas_etarias["60-64"] += 1
            elif 65 <= idade <= 69:
                faixas_etarias["65-69"] += 1
            elif idade >= 70:
                faixas_etarias["+70"] += 1
    
            #

def opcoes():
    parseFile()

    print("1 - Percentagem de doentes por sexo")
    print("2 - Percentagem de doentes por escalões de idade")
    print("3 - Percentagem de doentes por nível de colesterol")
    print("4 - Tabela ordenada por idade")
    print("5 - Sair")
    print("\n")
    opcao = input("Qual a sua opção? ")
    if int(opcao) == 1:
        print(sexos["M"])
        print(sexos["F"])

    if int(opcao) == 2: 
        print(f"30-34 anos: ", faixas_etarias["30-34"])
        print(f"35-39 anos: ", faixas_etarias["35-39"])
        print(f"40-44 anos: ", faixas_etarias["40-44"])
        print(f"45-49 anos: ", faixas_etarias["45-49"])
        print(f"50-54 anos: ", faixas_etarias["50-54"])
        print(f"55-59 anos: ", faixas_etarias["55-59"])
        print(f"60-64 anos: ", faixas_etarias["60-64"])
        print(f"65-69 anos: ", faixas_etarias["65-69"])
        print(f"  +70 anos: ", faixas_etarias["+70"])

    elif int(opcao) == 5:
        print("Adeus!")
    else:
        print("Opção inválida!")
        opcoes()

opcoes()
