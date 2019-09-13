from factoring import *
from ruffini import *
from simplify_test import *
from test_root import *

def find_roots(eq):
    roots= []
    max_expo = len(eq) - 1

    flag = True
    #Until all the roots have been found try to simplify anbd find roots
    while len(roots) != max_expo and flag == True:
        simplify(eq,roots)
        
        #If the equation have 0 or 1 as root, try to reduce the equation 
        if(len(roots) != 0):
            for i in roots:
                reduced_eq = ruffini(eq,i)
                if(reduced_eq != None):
                    reduced_eq.reverse()
                    eq = reduced_eq
        
        if(eq[0] != 0):
            factors = factoring(abs(eq[0]))
            if(factors != None):
                for i in factors:
                    is_root = test_is_root(eq, i)
                    if(is_root == False):
                        factors.remove(i)
                    else:
                        roots.append(i)

        print(roots)
        flag = False