"""
i = 0
wynik = 0

for i in range(1,20,4):              
 x = int(input("Podaj liczbe : "))
 wynik = wynik + x
 print(wynik)
"""
"""
a = input("a : ")
b = input("b : ")
c = int(a) + int(b)
print("wynie :",c)
"""

ppllist2 = [
            ('John', 27, 'Male'),
            ('John3', 22, 'Male'),
            ('John2', 11, 'Male')   
           ]

people2 = [
         {'id': 'IcFDG2bO9AYDF651DoyH', 'name': 'John', 'age': 27, 'sex': 'Male'},
         {'id': 'KcD9ntE6IRM59vkVta1k', 'name': 'Marie', 'age': 22, 'sex': 'Female'},
         {'id': 'yDlgcn99xPc19mYXcRmy', 'name': 'Agness', 'age': 25, 'sex': 'Female'}               
        ]

people = {
        "IcFDG2bO9AYDF651DoyH": {'name': 'John', 'age': 27, 'sex': 'Male'},
        "KcD9ntE6IRM59vkVta1k": {'name': 'Marie', 'age': 22, 'sex': 'Female'},
        "yDlgcn99xPc19mYXcRmy": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "cpQh6GiAbBdGv35NDoTk": {'name': 'Nabeel', 'age': 17, 'sex': 'Male'},
        "12BifzWxCQySKgLhgahC": {'name': 'Jasmin ', 'age': 42, 'sex': 'Female'},
        "QLnmg0pzlLj9x7c7DlLv": {'name': 'Ruby', 'age': 55, 'sex': 'Female'},
        "To47urX0DUznWmOxGZ6H": {'name': 'Lori', 'age': 27, 'sex': 'Male'},
        "KQ4bir3y4tlkbG69I7zq": {'name': 'Marie', 'age': 42, 'sex': 'Female'},
        "94cp4hsyZP2BnCh4D34z": {'name': 'Agness', 'age': 25, 'sex': 'Female'},
        "Vr4wRdkljeEs46Czxo54": {'name': 'Chiara', 'age': 17, 'sex': 'Male'},          
         }


for id, dictionary in people.items():
    print("ID", id)
    for key in dictionary:
        print(key, ":", dictionary[key])


"""
for name, age, sex in ppllist2:
    print(name, age, sex)

for record in ppllist2:
    print(record[0],record[2])

for id, dictionary in people.items():
    print("ID", id)
    for key in dictionary:
        print(key, ":", dictionary[key])

"""

