# [100%] FrogJmp
# Count minimal number of jumps from position X to Y.
# https://app.codility.com/demo/results/trainingX3893G-TWP/
def solution(X, Y, D):
    # write your code in Python 3.6
    dist = Y - X

    if dist <= 0:
        return 0
    else:
        if dist%D == 0:
            return dist // D 
        else:
            return dist // D + 1




##
# PermMissingElem
# Find the missing element in a given permutation.
# 100%
# https://app.codility.com/demo/results/trainingZBNP3T-8UW/
def solution(A):
    # write your code in Python 3.6
    if len(A)== 0:
        return 1
    if len(A) == 1:
        if A[0] == 1:
            return 2
        else: 
            return 1
    A.sort()
    N = len(A)

    if A[0] != 1:
        return 1
    if A[N-1] == N:
        return N+1

    for i in range(N):
        if i+1 != A[i]:
            return i+1
        i+=1




## 
# TapeEquilibrium
# Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])|.
# non-efficient solution
# https://app.codility.com/demo/results/trainingTJMJBN-GN7/
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
