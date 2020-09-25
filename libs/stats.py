
def promedio(l):
    suma = 0
    for i in l:
        suma += i
    
    
    return suma / len(l)


def mediana(l):
    
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2] + l[(len(l) // 2) - 1]) / 2
    


