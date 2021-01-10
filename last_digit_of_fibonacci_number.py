def last_num(n):
    i=0
    j=1
    for x in range(n-1):
        k = i+ j 
        k = k%10
        i = j 
        j = k 
    return(k)


print(last_num(7777))
