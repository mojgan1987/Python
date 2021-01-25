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
    
    
