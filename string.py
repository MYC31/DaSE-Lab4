

def sstr(str):
    rval = 0
    off, end = 0, 1
    for i in range(0, len(str)):
        j = i + 1
        while j < len(str) and str[j] == str[j-1]:
            j = j + 1
        if j - i > end - off:
            rval = 1
            off, end = i, j
    print(str[off:end])
    return rval


#if len(substr) > 1, return 1; else return 0
val = sstr("abccccda")
print(val)

