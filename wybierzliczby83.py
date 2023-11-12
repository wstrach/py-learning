# z przedziału 100-470 wybierz liczby podzielne przez 7, ale niepodzielne przez 5

# lista generująca []
numbers83 = [
liczba 
for liczba in range(100,471)
    if (liczba % 8 == 0) and (liczba % 3 != 0)
]        

numbers57 = [
liczba 
for liczba in range(100,471)
    if (liczba % 7 == 0) and (liczba % 5 != 0)
]        
        
print (numbers57)
print (numbers83)


