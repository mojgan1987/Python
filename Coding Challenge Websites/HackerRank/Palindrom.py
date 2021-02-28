# find all palindrom
def mojpa(S):
    
    n=len(S)
    
    palins = []
    for i in range(0,n):
        for j in range(i+1,n):
            sbs = S[i:j]
            
            if sbs == sbs[::-1]:
                palins.append(sbs)
                
    print(max(palins,key=len))
    return palins
