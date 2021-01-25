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
"--".join(['a','b','c'])

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
#casting a list to a set1
set(mylist)
set('Mississippi')

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