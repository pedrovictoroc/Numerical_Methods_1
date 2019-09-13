def ruffini(eq, root):
    eq.reverse()
    cont = eq[0]
    res = []
    res.append(cont)

    for i in range(0, len(eq)-1):
        cont = root*cont + eq[i+1]
        res.append(cont)

    if (cont == 0):
        res.pop()
        return res
    
    return None