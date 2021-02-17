# OddOccurrencesInArray
# Find value that occurs in odd number of elements.
# 66%
# https://app.codility.com/demo/results/trainingYR24TE-Q95/
# O(N**2)
def solution(A):
    # write your code in Python 3.6
    A.sort()
    myset = set(A)

    counts = []
    for item in myset:
        if A.count(item)%2 == 1:
            return item
          
          
          
##
# CyclicRotation
# Rotate an array to the right by a given number of steps.
# 87%
# https://app.codility.com/demo/results/training9YSVR2-KKS/
def solution(A, K):
    # write your code in Python 3.6
    N = len(A)
    if N == 0:
      return 0

    r = K%N
    if r == 0:
        return A
    else:
        arr = A[-r:]
        arr.extend(A[:N-r])

        return arr
