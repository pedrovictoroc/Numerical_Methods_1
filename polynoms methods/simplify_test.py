def simplify(eq,factors):
    coeficient = 0
    #Test the coeficient sum, if 0, then the equation have 1 as a root
    for i in range(0, len(eq)):
        coeficient += eq[i]
    
    if(coeficient == 0):
        factors.append(1)
    
    #Test the free term, if 0, then then equation have 0 as a root
    if(eq[0] == 0):
        factors.append(0)