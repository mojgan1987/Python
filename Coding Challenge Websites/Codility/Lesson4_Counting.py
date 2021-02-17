# FrogRiverOne
# Find the earliest time when a frog can jump to the other side of a river.
# 72% timeout
# https://app.codility.com/demo/results/trainingVZK4MH-ZRE/
def solution(X, A):
    # write your code in Python 3.6
    if len(A) == 1:
        if X==1 and A[0] == 1:
            return 0
        else:
            return -1
    
    tmp = [0] * X
    i = 0
    for item in A:
        tmp[item-1] = item
        if 0 not in tmp:
            return i 
        i+=1
        if i == len(A):
            return -1
            
            
            
##
# PermCheck
# Check whether array A is a permutation.
# 83%
# https://app.codility.com/demo/results/training78T35M-QA8/
# wrong answer: [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]
def solution(A):
    # write your code in Python 3.6
    n = len(A)
    overal_sum =  (n*(n+1))/2

    if n == 1:
        if A[0] == 1:
            return 1
        else:
            return 0

    if sum(A) != overal_sum:
        return 0
    else:
        A.sort()
        if A[0] == 1 and A[-1] == n:
            return 1
        else:
            return 0
# 100 %
# https://app.codility.com/demo/results/trainingNWUZU5-AYS/
def solution(A):
    # write your code in Python 3.6
    n = len(A)
    overal_sum =  (n*(n+1))/2

    if n == 1:
        if A[0] == 1:
            return 1
        else:
            return 0

    if sum(A) != overal_sum:
        return 0
    else:
        if len(set(A)) != n:
            return 0
        A.sort()
        if A[0] == 1 and A[-1] == n:
            return 1
        else:
            return 0
            
            
## 
# MaxCounters
# Calculate the values of counters after applying all alternating operations: increase counter by 1; set value of all counters to current maximum.
# 66 %
# https://app.codility.com/demo/results/trainingGDZ2W7-MEB/
# timeout
def solution(N, A):
    # write your code in Python 3.6
    outp = [0] * N
    for item in A:
        if item == N+1:
            maxc = max(outp)
            outp = [maxc] * N
        else:
            outp[item-1] += 1
    return outp
