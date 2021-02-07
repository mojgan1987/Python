# Time out on two cases out of 21
def checkMagazine(magazine, note):
    
    flag = False
    for word in note:
        if word not in magazine:
            flag = True
            break
        else:
            magazine.remove(word)
            
    if flag:
        print("No")
    else:
        print("Yes")

# using Counters

from collections import Counter
def checkMagazine(magazine, note):
    
    mag = Counter(magazine)
    notes = Counter(note)
    
    flag = True
    for n in notes:
        if notes[n] > mag[n]:
            flag = False
            break

    if flag:
        print("Yes")
    else:
        print("No")



def twoStrings(s1, s2):
    
    s_1 = Counter(s1)
    s_2 = Counter(s2)
    
    intersect = s_1 & s_2
    
    if len(intersect) == 0:
        return "NO"
    else:
        return "YES"
