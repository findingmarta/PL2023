
def main():
    texto = input("Texto: \n")
    texto = texto.lower()
    On = False
    total = 0
    i = 0

    while i != len(texto):
        if texto[i] == "=":
            print(f"A soma dos números encontrados é: {total}") 
            i += 1
        else:
            if On:
                if texto[i].isdigit():
                    j = i
                    while j < len(texto) and texto[j].isdigit():
                        j += 1
                    total += int(texto[i:j])
                    i = j
            
            if texto[i:i+2] == "on":
                On = True
                i += 2
            elif texto[i:i+3] == "off":
                On = False
                i += 3
            else:
                i += 1
        
        
main()

# on1off222==off333 on123=444on 555 =on666off=2=
# 111 off 222 = off 333 on = 444 on 555 = on 666 off = 2