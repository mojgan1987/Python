##
# Pair Socks
# https://www.hackerrank.com/challenges/sock-merchant/
def sockMerchant(n, ar):
    uniq = set(ar)
    
    tmp = 0
    for color in uniq:
        tmp += ar.count(color)//2
    
    return (tmp)


##  
# Valley counting
# https://www.hackerrank.com/challenges/counting-valleys/
def countingValleys(steps, path):
    path = list(path)
    tmp = 0
    vcounter = 0
    vflag = 0
    for i in range(0,steps):
        if path[i] == 'D':
            tmp += -1
        else:
            tmp += 1
        
        if tmp == -1:
            vflag = 1
        
        if tmp == 0 and vflag == 1:
            vcounter+=1
            vflag = 0

    return vcounter

  
##
# Jumping Clouds
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/
def jumpingOnClouds(c):
    
    if len(c) == 2:
        return 1
    if len(c) == 1:
        return 0
    
    i=0
    if c[i+2] != 1:
        return 1 + jumpingOnClouds(c[i+2:])
    else:
        return 1 + jumpingOnClouds(c[i+1:])

##
# Repeated String
# https://www.hackerrank.com/challenges/repeated-string/
def repeatedString(s, n):
        
    length = len(s)
    
    d = n//length
    r = n%length

    count = s.count('a')
    r_count = 0
    if r!=0:
        r_count = s[:r].count('a')

    return (count*d) + r_count
