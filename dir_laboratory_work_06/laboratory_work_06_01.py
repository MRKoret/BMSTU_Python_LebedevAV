from math import (sin,cos,sqrt,pi)

def z1(alpha):
    return cos(alpha) + sin(alpha) + cos(3 * alpha) + sin(3 * alpha)
def z2(alpha):
    return 2 * sqrt(2) * cos(alpha) * sin((pi / 4) + 2 * alpha)

num = [0,30,45,60,90,180]
with open(('input.txt'), 'wt') as inp:
    for i in num:
        print(i, file=inp)

with open(('input.txt')) as inp:
    with open(('output.txt'), 'wt') as out:
        for line in inp:
            alpha = float(line.strip())
            res1 = z1(alpha)
            res2 = z2(alpha)
            print("{0:3.0f}: z1 = {1: 1.2f}, z2 = {2: 1.2f}".format(alpha,res1,res2), file=out)
