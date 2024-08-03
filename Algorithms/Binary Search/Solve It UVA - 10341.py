


from math import e, sin, cos, tan
from sys import stdin


def equation(x):
    return p *e **-x + q *sin(x)+r * cos(x) + s*tan(x) + t*x **2 +u

def bisection():
    low,high = 0,1
    while low + 1e-7 < high:
       x = (low+high)/2
       if equation(low) * equation(x) <= 0 :
           high =x
        else:
           low = x
    return (low + high)/2

for line in stdin:
    p,q,r,s,t,u = map(int, line.split())
    if equation(0)*equation(1) > 0 :
        print("No solution")
    else:
        print(f"{bisection():.4f}")




