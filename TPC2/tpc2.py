from sys import stdin

def main():
    On = False
    total = 0

    for texto in stdin:
        texto = texto.lower()
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
                        i = j - 1
                        
                if texto[i:i+2] == "on":
                    On = True
                    i += 2
                elif texto[i:i+3] == "off":
                    On = False
                    i += 3
                else:
                    i += 1
         
main()

# TESTAR
# jpdf20ahon100=40adsffasd oFF32 On=18On=On
# on1oFf222==off333 ON123=444on 555 =on666off=2=
# 111 off 222 = off 333 on = 444 on 555 = on 666 off = 2