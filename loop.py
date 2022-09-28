

l = [1,2,3,4,5]


#for loop
for i in range(len(l)-1, -1, -1):
    print(l[i], end = " ")


#while loop
i = len(l) - 1
while i >= 0:
    print(l[i], end = " ")
    i = i - 1
