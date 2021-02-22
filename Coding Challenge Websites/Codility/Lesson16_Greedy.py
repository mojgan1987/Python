MaxNonoverlappingSegments
Find a maximal set of non-overlapping segments.
# 90%: error: check for empty input
# https://app.codility.com/demo/results/trainingJESVVY-FAF/
def solution(A, B):
    # write your code in Python 3.6

    if len(A) == 1:
        return 1

    min_start = A[0]
    min_end = B[0]
    n = 1

    for i in range(1, len(A)):
        # print(f'i={i}')
        # print(f'min_start={min_start}')
        # print(f'min_end={min_end}')
        if B[i] > min_end:
            if A[i] > min_end:
                min_start = A[i]
                min_end = B[i]
                # print(f'min_start={min_start}')
                # print(f'min_end={min_end}')
                n+=1
                # print(f'n={n}')
    
    return n
    
    
# TieRopes
# Wrong Answer, server down
def solution(K, A):
    # write your code in Python 3.6
    
    n=len(A)
    tmp = 0    
    cnt = 0

    if n==1:
        if A[0] >= K:
            return 1
        else:
            return 0

    for i in range(n-1):
        if A[i] >= K:
            cnt+=1
        tmp+=A[i]
        if tmp>K:
            cnt+=1
            tmp=0
    return cnt
