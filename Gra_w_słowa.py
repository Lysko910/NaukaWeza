import random
random.seed()

def get_quote(set_of_quotes):
    random.seed()
    return set_of_quotes[random.randint(0, random.randint(0, len(set_of_quotes)-1))]

def add_quote(set_of_quotes):
    while(True):
        qoute = input("Podaj słowo do wprowadzenia: ")
        if qoute.isalpha():
            break
        print("Wprowadź poprawny takst")
    set_of_quotes.append(qoute.upper())
    return set_of_quotes

def remove_quote(set_of_quotes):
    new_set_of_quotes = []
    quote = input("Wpisz słowo które usunąć: ").upper()
    for q in set_of_quotes:
        if q != quote:
            new_set_of_quotes.append(q)
        else:
            pass
    return new_set_of_quotes

if __name__ == "__main__":
    set_of_quotes = ["PIETRUSZKA", "OKO", "OPEL","ANNA","PSZCZYNA","BANAN"]
    kwoty = [[100, "100zł"], [150, "150zł"], [200, "200zł"], [300, "300zł"], [500, "500zł"]]
    Wygrana = 0
    correct_spl=['A','O','U','I','E','Y']
    print("wylosowane słwo:{}\t\n", get_quote(set_of_quotes))
    print("Zestaw : {} \n",set_of_quotes)

    set_of_quotes = add_quote(set_of_quotes)
    print("Zestaw : {} \n", set_of_quotes)

    set_of_quotes= remove_quote(set_of_quotes)
    print("Zestaw : {} \n", set_of_quotes)

    print("Dobra\n Zagrajmy w gre !!")
    Instance = get_quote(set_of_quotes)
    print("to wylosowalem: {}",Instance)
    empty =[]
    for i in Instance:
        empty.append("_");
    string = " ".join(str(x) for x in empty)
    print(string)
    used =[]
    while True:
        print( "{-\.*./--\.*./--\.*./--\.*./--\.*./--\.*./--\.*./--\.*./--\.*./--\.*./--\.*./-}")
        i = random.randint(0, len(kwoty)-1)
        zl_val = kwoty[i][0]
        zl = kwoty[i][1]
        print(f"Wylosowana kwota :{zl}")

        spl = input("Podaj spółgłoskę: ").upper()
        if spl in correct_spl or not len(spl) == 1:
            print("Podaj poprawną spółgłoskę")
        elif spl in used:
            print("Podaj nie używaną litere ")
        else:
            for x in Instance:
                if x == spl:
                    indx = Instance.index(spl)
                    empty.insert(indx,spl)
                    empty.pop(indx+1)
                    Wygrana+=zl_val

            if spl not in Instance:
                print("Próbuj dalej")
        if spl in Instance:
            used.append(spl)

        string = " ".join(str(x) for x in empty)
        print(string)
        print("Obecna wygrana{}",Wygrana)

        if all(elem in used+correct_spl for elem in Instance) :
            break
    print("MUSISZ ZGADYWAĆ!!!")
    print("Masz 3 szanse!!!")
    for v in range(3):
        slw =input("Podaj Słowo : ").upper()
        if slw == Instance:
            print("#-#-# Brawo ty #-#-#")
            break
        print("Masz jeszcze: ",3-v," szans")

    print("#-#-# Koniec #-#-#")

