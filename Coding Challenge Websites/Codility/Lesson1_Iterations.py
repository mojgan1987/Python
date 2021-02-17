# [100%] BinaryGap
# Find longest sequence of zeros in binary representation of an integer.
def solution(N):
    # to-do:
    # check if the number is power of 2
        # return 0

    # trivial solution
    n = bin(N)

    maxl = 0
    i = -1
    flag = True
    length = 0
    
    for char in n[2:]:
        i+=1
        char = int(char)
        if char == 0 and flag:
            pass
        elif char == 1 and flag:
            flag = False    
        elif char == 0 and not flag:
            length +=1
            # print(length)
        elif char == 1 and not flag:
            maxl = max(maxl,length)
            length = 0
    return maxl
