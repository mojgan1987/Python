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
    
