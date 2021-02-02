## Strings 
# Step size:
mystr = 'abcdefghijk'

mystr[2:9:3] #output: cfi

# use step size to reverse the string 
mystr[::-1]

# string formatting
print('Check the order: {c} {b} {a}'.format(a='1', b='2', c='3'))

# formatting floats
result = 199/222
print('The result is {r:20.4f}'.format(r=result))

# formatted string literals
name = 'Moj'
print(f'My name is {name}')
print(f'My name is {name!r}')

x,y='something','more'
print("insert %s here and %s here"%(x,y))

print("'%s' and '%r' difference")
print("%s and %r"%('\thi','\tthere'))

# string alignment
print('{0:=<8} | {1:.^8} | {2:->8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))


# useful String functions
s.replace()
s.isupper()
s.find()
s.center(total_len, char)
s.capitalize() #1st letter
s.title()
s.istitle()
s.isalnum()
s.isalpha()
s.isspace()
s.endswith(sth)
s.partitin(sth) 
"--".join(['a','b','c'])
'\t'.expandtabs()


##
# LIST
# useful functions
mylist.extend(iterable)
mylist.insert(index, item)
mylist.remove()
mylist.reverse()
mylist.sort()


##
# SETS
myset = set()
myset.add()
set(mylist) #casting a list to a set1
set('Mississippi')
myset.discard(sth)
set1.difference(set2)
s1.difference_update(s2)
s1.intersecton(s2)
s1.intersecton_update(s2)
s1.isdisjoint(s2)# true if null intersection
# elements exactly in one fo the sets
s1.symmetric_difference(s2)


##
# I/O
myfile.read()
myfile.seek(0)
myfile.read()
myfile.seek(0)
myfile.readlines()

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()


##
# Useful Python functions
bin(digit) # returtns binary string
range(start, end, stepsize)
b = None
enumerate(iterable)
zip(mylist1,mylist2)
x in mylist
map(function, input)
filter(function, input)


## Numbers
hex(number)
bin(number)
pow(n1,n2,mod)

