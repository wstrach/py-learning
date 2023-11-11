import sys

lista = [1, 2, 3, 4, 5, 6, 7]

print("lista -", lista)

listaDoPotegi = ([element**2 for element in lista])

print("do potęgi -", listaDoPotegi)

liczbyParzyste = [element
                  for element in lista
                  if element %2 == 0
                 ]  

print("liczby parzyste z listy -",liczbyParzyste)

potegiLiczbzZakresu = [element**2
                       for element in range(1,51)
                      ]
print(potegiLiczbzZakresu)

eventNumbers = [nums 
                for nums in range(1,500)
                if nums %2 == 0
               ]

print("evetNumbers -",eventNumbers)
print(sys.getsizeof(eventNumbers))

eventNumbersGen = (numsGen 
                   for numsGen in range(1,500)
                   if numsGen %2 == 0
                  )

for item in eventNumbersGen: print(item)
print(sys.getsizeof(eventNumbersGen))



