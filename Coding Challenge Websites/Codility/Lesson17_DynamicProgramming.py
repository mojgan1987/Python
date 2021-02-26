# MinAbsSum
# Given array of integers, find the lowest absolute sum of elements.
# WRONG
def solution(A):
    # write your code in Python 3.6
    # sum of 0 elements = 0
    if len(A) == 0:
        return 0
    else:
        # print(A)
        for i in range(len(A)):
            # print(i)
            # print(A[i])
            return min(abs(A[i]+solution(A[i+1:])) , abs(-1*A[i] + solution(A[i+1:])) )
