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

        
        
        
##
# minimum swaps
# https://www.hackerrank.com/challenges/minimum-swaps-2/
def minimumSwaps(arr):
    
    if len(arr) == 1:
        return 0
    
    minitem = min(arr)
    indx = arr.index(minitem)
    print(f'index={indx}')
    new_arr = arr
    new_arr[indx] = arr[0]
    print(f'new={new_arr}')
    
    if indx == 0:
        return 0 + minimumSwaps(new_arr[1:])
    else:
        return 1 + minimumSwaps(new_arr[1:])

    
    
    
# Wrong asnwer in 10 out of 16 cases
#
#
def arrayManipulation(n, queries):
    
    orig = []
    for i in range(0,n):
        orig.append(0)
        
    for query in queries:
        a = query[0]
        b = query[1]
        k = query[2]
        
        for j in range(a-1,b):
            orig[j] += k
        print(orig)

    return max(orig)
