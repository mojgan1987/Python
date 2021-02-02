# OOP Special functions (Magic/Dunder)
    def __str__(self):
        return "Must Return a string, may use self.attribs"

    def __len__(self):
        return self.attrib

    def __del__(self):
        print("print a message after deletion")


## Function Excercises        
# return all even numbers in a list
def return_all_even(num_list):
    return [num for num in num_list if num%2==0]

# takes a string and return another string where chars in even position are upper and odd postion are lower case
def myfunc(myst):
    c = -1
    tmp_st = ''
    for char in myst:
        c+=1
        if c%2== 0:
            tmp_st += char.upper()
        else:
            tmp_st += char
    return tmp_st

# reverse words order in a string
def reverse_words(text):
    words = text.split()
    rev_text = words[::-1]
    return " ".join(rev_text)

 # return sum except numbers between 6 followed by 9   
def summer_69(arr):
    tmp = 0
    add = True
    for num in arr:
        while add:
            if num !=6:
                tmp += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return tmp

# print and count prime numbers up to num
def count_primes2(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in primes:  # use the primes list!
            if x%y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(primes)
    return len(primes)                

# count in index = value
def count_match_index(L):
    return len([num for count,num in enumerate(L) if  count==num])
