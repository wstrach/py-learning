ran=100

for i in range(0,ran):
    if i == 0 :
       pri=0
       print("inkr",i, "ciąg Fib", pri)
    if i == 1 :
       sec=1
       print("inkr",i, "ciąg Fib", sec)
    if i > 1 :
       thi=pri+sec
       print("inkr",i, "ciąg Fib", thi)
       pri=sec
       sec=thi
       thi=pri+sec
        
        
