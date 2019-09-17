from solve_equation import *

def bissection (func,a,b,error,maxIte):
    fa = solver(func,a)
    fb = solver(func,b)

    if (fa*fb > 0):
        raise ValueError("Intervalo não varia de sinal")

    interval = abs(b-a)
    index = 0
    while interval > error or index <= maxIte:
        x = (a+b)/2
        fx = solver(func,x)

        print("a: {} | fa: {} | b: {} | fb: {} | x: {} | fx: {} | i: {}".format(a,fa,b,fb,x,fx,index))

        if(fa*fx >0):
            a = x
            fa = fx
        else:
            b = x
            fb = fx
        
        interval = interval / 2
        
        index += 1
    
    return x