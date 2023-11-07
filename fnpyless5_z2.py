#zadanie 2.1
imie = input("Imię ")
nazwisko = input("Nazwisko ")
nrtelefonu = input("Nr telefonu ")
nrtelefonu=nrtelefonu.replace("-","")
nrtelefonu=nrtelefonu.replace(" ","")
print(imie.title(),nazwisko.title(),nrtelefonu)

#print("Imię", imie.isalpha())
#print("Nazwisko",nazwisko.isalpha())
#print("nr telefonu",nrtelefonu.isnumeric())

print("Czy kobieta? ", "a"==imie[-1]) 

