# [100%] FrogJmp
# Count minimal number of jumps from position X to Y.











## 
# TapeEquilibrium
# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
# non-efficient solution
def solution(A):
    # write your code in Python 3.6
    N = len(A)

    if N==2:
        return abs(A[0]-A[1])

    # non-efficient
    minm = float('inf') 
    for i in range(2,N-1):
        tmp = abs(sum(A[:i])-sum(A[i:]))
        minm = min(minm, tmp)
    
    return minm
