## Some quick notes ##

##
# COllections

# Counters: n of unique values in a list
from colections import Counter
tocheck = [some repated intems], or string
Counter(tocheck) # out: a dictionary subclass

c = Counter(bla)
c.most_common(tops)

# Defult Dictionary
from colections import defaultdict
d  = defaultdict(lambda: 0)
d['bla'] # returns 0


from colections import namedTuple
# a combination of tuples and class objects!

## File I/O
# shutil and OS
import os
os.getcwd()
os.listdir(path)

# move files
import shutil
shutil.move(src,dst)

#del
os.unlink(path)
os.rmdir(path)
os.rmtree(path)
# pip install send2trash

# look within directories and subdirctories: 
for folder , sub_folders , files in os.walk()


## DATETIME
import datetime
today = datetime.date.today()
from datetime import datetime

# Math and random
# Sample with replacement
random.choices(list, counts)
# Sample WITHOUT replacement
random.sample(list, counts)

## Regular Expressions
# ^ start, $ end, [^]+ exclude
re.search(pattern, text): the first match
re.findall(pattern, text): all matches
re.finditer(): to iterate
match.group() # returns the fond pattern
re.compile(group of patterns)

# Timing
import time
time.time() # current time

import timeit
timeit.timet(statement, setup, number)

%%timeit #Jupyter Notebook magic


## Zip/Unzip
import zipfile
zipfile.ZipFile(name, mode)
.write .close .extractall()

import shutil
shutil.make_archive(name, format, dir)
shutil.unpack_archive(name, dir, format)


