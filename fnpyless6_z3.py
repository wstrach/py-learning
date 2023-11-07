a=input("a : ")
b=input("b : ")
c=input("c : ")

print("a:",a,"b:",b,"c:",c)


if a > b and a > c and b > c :    
  print("abc ",a,",",b,",",c)
elif a > b and a > c and c > b :  
  print("acb ",a,",",c,",",b)  
elif b > a and b > c and a > c :
  print("bac ",b,",",a,",",c)  
elif b > a and b > c and c > a : 
  print("bca ",b,",",c,",",a)    
elif c > a and c > b and a > b :
  print("cab ",c,",",a,",",b)    
elif c > a and c > b and b > a : 
  print("cba ",c,",",b,",",a)
