i =0
s = input()
while i in range(len(s)) :
    temp = s[i]
    k = i+1
    c = 1
    while k<len(s) :
        if s[k] != temp:
            break
        c += 1        
        k += 1
    print((c,int(s[i])),end=' ')
    i = k
