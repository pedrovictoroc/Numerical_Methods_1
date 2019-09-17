def solver(eq,num):
    cont = 0
    for i in range(0, len(eq)):
        cont += eq[i]*(num**i)
    
    return cont