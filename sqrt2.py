

def libsqrt1():
    return pow(2, 0.5)


def binarySearch():
    rval = 1
    epsilon = 0.0000001
    dif = rval*rval - 2
    while abs(dif) >= epsilon:
        if dif > 0:
            rval = rval - rval / 2
        else:
            rval = rval + rval / 2
        dif = rval*rval - 2
    return rval


"""
y = xx - 2
y' = 2x; 
yy = 2x + c; 
select g to be starting point
gg - 2 = 2g + c
c = gg - 2g - 2
yy = 2x + gg -2g - 2
0 = 2x + gg -2g - 2
x = (-gg + 2g + 2) / 2 
"""
def NewTon():
    x = 1
    epsilon = 0.0000001
    while abs(x*x - 2) >= epsilon:
        x = (-x*x + 2*x + 2) / 2
    return x


print(NewTon())