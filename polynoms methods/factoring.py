def factoring(num):
    res = []

    #Base cases
    if (num == 2 or num == 3):
        return num
    
    for i in range(2,int(num/2)+1):
        if ((num/i) - int(num/i) == 0):
            res.append(i)
    
    if (len(res) == 0):
        return None
    
    return res