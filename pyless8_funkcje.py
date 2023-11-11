import os

cmd="git --version"
os.system(cmd)

def sayhallo(imie) :
    print("hello", imie)

def lista_korzysci(nr_zdania) :
    lista = ["Lepiej zorganizowany kod","Wieksza czytelnosc kodu","Latwiejsze wielokrotne uzycie kodu","Mozliwosc dzielenia sie kodem i laczenia go w calosc przez rozne osoby"]
    print(lista[nr_zdania])

def buduj_zdanie(nr) :
    print(lista_korzysci(nr), "jest zaleta funkcji")

zdanie=input("Podaj nr zdania : ")

buduj_zdanie(int(zdanie))






