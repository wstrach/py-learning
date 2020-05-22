a=input("bok a : ")
b=input("bok b : ")
c=input("bok c : ")

print("a:",a,"b:",b,"c:",c)

if int(a) > 0 and int(b) > 0 and int(c) > 0 :
 print("z podanych boków abc można utworzyć trójkąt")

a2=int(a)**2
b2=int(b)**2
c2=int(c)**2

print("a2:",a2 ,"b2:",b2 ,"c2:",c2)

if ((a2 + b2) == c2) or ((a2 + c2) == b2) or ((b2 + c2) == a2):
  print("TAK - a2:",a2 ,"b2:",b2 ,"c2:",c2)
else :   
  print("NIE - a2:",a2 ,"b2:",b2 ,"c2:",c2)