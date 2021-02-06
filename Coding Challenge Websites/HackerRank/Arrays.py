## 
# hourglass
# https://www.hackerrank.com/challenges/2d-array/
def hourglassSum(arr):
    maxr=-324
    for j in range(0,4):
        for i in range(0,4):
            r1 = arr[j][0+i:3+i]
            r2 = arr[j+1][1+i]
            r3 = arr[j+2][0+i:3+i]
            hsum = sum(r1)+r2+sum(r3)
            maxr = max(maxr,hsum)
            
    return maxr


##
# Left rotation
# https://www.hackerrank.com/challenges/ctci-array-left-rotation/
def rotLeft(a, d):
    n = len(a)
    print(n)
    r = d%n
    print(r)
    
    
    new_arr = []
    
    new_arr[:n-r] = a[r:]
    new_arr[n-r:] = a[:r]
    
    return new_arr

##
# Bribe
# https://www.hackerrank.com/challenges/new-year-chaos/
def minimumBribes(q):
    
    bribes = 0     
    flag = True
    for i in range(0,len(q)):
        if q[i]-i >= 4:
            flag = False
            break
        else:
            for j in range(i,len(q)):
                if q[j] < q[i]:
                    bribes += 1 
                
    if flag:
        print(bribes)
    else:
        print('Too chaotic')
