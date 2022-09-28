import random


def function(x):
    return pow(x, 3) + pow(x, 2)


def integral(off, end, floor, ceil):
    N = 10000000
    count = 0
    for i in range(0, N):
        x = random.uniform(off, end)
        y = random.uniform(floor, ceil)
        if function(x) >= y:
            count = count + 1
    return (count / N) * (end - off) * (ceil - floor)


print(integral(0, 1, 0, 2))
# print(function(0.5))