def pole_prostokata(a, b):
    if (a==0) or (b==0):
        return "jedna z wartości = 0"
    return (a*b)

poleA=pole_prostokata(4,0)
poleB=pole_prostokata(5,5)

print("poleA : ", poleA)
print("poleB : ", poleB)