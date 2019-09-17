#An version of the bissection algorithm, unfortnatelly this method execute in more time than the original
#time to compare: Original: 0.0004723072052001953 This: 0.0002791881561279297
#Variable values: func = [-30,31,-10,1] a = 0   b = 3   e = 0.00000001  maxIte = 10

from solve_equation import *

def altered_bissection (func,a,b,error,maxIte):

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

        l_x = (a+x)/2
        fl_x = solver(func,l_x)

        r_x = (x+b)/2
        fr_x = solver(func,r_x)

        if(abs(fl_x) < abs(fr_x)):
            interval = (x-a)
            b = x
            fb = fx
        else:
            interval = (b-x)
            a = x
            fa = fx

        index += 1
    
    return x