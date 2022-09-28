

mul = 1
for i in range(1, 101, 2):
    print(i, end = " ")
    if i < 50:
        mul  = mul * i
print("\n", mul)