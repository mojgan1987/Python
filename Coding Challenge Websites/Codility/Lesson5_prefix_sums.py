## Mushroom Picker
def prefix_sum(A):
    n = len(A)
    p = [0] * n
    p[0] = A[0]
    for i in range(1,n):
        p[i] = p[i-1] + A[i]
    return p
    
def mid_sum(p, x, y):
    return p[y]-p[x-1]
    
def mushroom_picker(A,k,m):
    n= len(A)
    mushrooms = 0
    pref_sum = prefix_sum(A)
    print(pref_sum)
    
    # left
    for p in range(min(m,k)+1):
        print(f'p={p}')
        left_p = k-p
        print(f'left_p={left_p}')
        right_p = min(n-1, max(k,k+m-2*p))
        print(f'right_p={right_p}')
        print(f'mushrooms={mid_sum(pref_sum,left_p,right_p)}')
        mushrooms = max(mushrooms, mid_sum(pref_sum,left_p,right_p))
    print()
    # right
    for p in range(min(m+1,n-k)):
        print(f'p={p}')
        right_p = k+p
        print(f'right_p={right_p}')
        left_p = max(0, min(k, k- (m-2*p)))
        print(f'left_p={left_p}')
        print(f'mushrooms={mid_sum(pref_sum,left_p,right_p)}')
        mushrooms = max(mushrooms, mid_sum(pref_sum,left_p,right_p))
        
    return mushrooms


##
## CountDiv
# Compute number of integers divisible by k in range [a..b].
# 100% https://app.codility.com/demo/results/training4X6SN8-M7Z/
def solution(A, B, K):
    # write your code in Python 3.6
    min_div = 0
    if A%K==0:
        min_div = A
    else:
        min_div = (A//K+1)*K
    # print(min_div)
    max_div = (B//K)*K
    # print(max_div)

    # print(int(((max_div-min_div)/K)+1))
    return int((max_div-min_div)/K+1)
    
    
##
# GenomicRangeQuery
# Find the minimal nucleotide from a range of sequence DNA.
# 100% https://app.codility.com/demo/results/trainingEW3B7M-MZY/
def solution(S, P, Q):
# write your code in Python 3.6
# non-empty string
# check size of P Q
# if len(P) != len(Q):
#     return -1

M = len(P)
results = [0]*M

gens = {'A':1, 'C':2, 'G':3, 'T':4}

if M == 1:
    results[0] = gens[S[0]]
    # print(results)

for item in range(M):
    # print(item)
    st = S[P[item]:Q[item]+1]
    if 'A' in st:
        results[item] = 1
    elif 'C' in st:
        results[item] = 2
    elif 'G' in st:
        results[item] = 3
    elif 'T' in st:
        results[item] = 4
return results

