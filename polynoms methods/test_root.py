def test_is_root(eq,num):
    cont = 0
    for i in range(0, len(eq)):
        cont += eq[i]*(num**i)
    
    if (cont == 0):
        return True
    
    return False