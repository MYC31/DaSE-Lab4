import math
import random


def sqrt2():
    return math.sqrt(2)


"""
    反正切级数，收敛速度极慢，需要628项才能收敛到小数点后2位。
"""
def series():
    N = 999999999
    sum = 0
    sign = 1
    for i in range(1, N+1):
        sum = sum + sign / (2*i-1)
        sign = sign * -1
    return 4 * sum


"""
    蒙特卡洛法，因为使用了伪随机数，所以精度有限。
"""
def integral():
    N = 10000000
    count = 0
    for i in range(0, N):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if pow(x, 2) + pow(y, 2) <= 1:
            count = count + 1
    return 4 * count / N


"""
    拉马努金级数，收敛速度极快，仅需两项就可以精确到小数点后10位。
"""
def Ramanujan():
    sum = 0
    N = 5
    for i in range(0, N):
        sum = sum + (math.factorial(4*i)/pow(math.factorial(i), 4)) * (26390*i+1103) / pow(396, 4*i)
    return 1 / (2*math.sqrt(2) / 9801 * sum)


"""
    反余弦级数，9项就可以精确到小数点后8位，收敛速度较快   
"""
def Newton():
    N = 1000
    rval = 1 / 2
    dfac1, dfac2 = 1, 1
    p = 2
    for i in range(1, N+1):
        dfac1 = dfac1 * ((i << 1) + 1)
        dfac2 = dfac2 * (i << 1)
        p = p << 2
        rval = rval + dfac1 / (dfac2 * pow((i << 1)+1, 2) * p)
    return 6 * rval


print(Newton())












