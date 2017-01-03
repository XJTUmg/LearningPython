#!/usr/bin/python

import math

############################
#          basic           #
############################

# plz use raw_input

x = 1
print "x = " + `x`

print 'C:\\now'
print r'C:\now' # raw string
# print r'C:\' will produce error
# print r'C:\\' is ok
print u'python' # Unicode string 16bit 

lis = 'Hello'
print lis[-1] # loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers[1 : 3] # will print [2, 3]
print numbers[ : 2]
print numbers[6 : ]
print numbers[0 : 10 : 2] # will print [1, 3, 5, 7, 9]
print numbers[8 : 3 : -1] # will print [9, 8, 7, 6, 5]
# print [1, 2, 3] + 'world' will produce error, different type
print 3 in numbers # will print True/False
print len(numbers), min(numbers), max(numbers) # will print '10 1 10'

name = list('Perl') 
name[1 : ] = list('thon') # replace the slice
name[1 : 1] = list('y') # insert elements
print name # will print 'python'

############################
#  list: mutable sequences #
############################

lst = [1, 2, 3]
lst.append(4) # append 4 to the end of lst
lst.extend([3, 6]) # append a list to the end of lst
lst.count(3) # count the occurrences of an element in a list
lst.index(3) # find the index of the first occurrence of a value
lst.insert(2, 3) # insert(index, value)
lst.pop(0) # del an element (by default, the last one) and return it
lst.remove(3) # remove(value), only remove the first occurrence of the value
lst.reverse() # just reverse the element in the list
lst.sort() #sort doesn't return a list
lst = sorted(lst) # sorted return a list
name.sort(key = len) # sorted according to the len
lst.sort(reverse = True) #same as lst.sort() lst.reverse()

############################
#tuple: immutable sequences#
############################

tup1 = tuple([1, 2, 3]) #same as list
tup = (42, ) # must have comma
             # the tuple function works in pretty much the same way as list

############################
#         strings          #
############################

#!!!!strings are immutable!!!!

form = "%s, %s"
vals = ('Hi', 'all')
print form % vals # string formatting, similar to 'scanf' in C
print '%-10.2f' % math.pi # (-) left-aligns the value
print '%+d' % 10 # (+) output a sign, will print '+10'
print '%.*s' % (5, '1234567') # (*) set the width

S = 'ababac'
S.find('ab') # return the leftmost index, if it is not found, -1 is returned
S.find('ab', 1, 4) # supplying start and end

seq = ['1', '2', '3', '4', '5']
sep = '+'
print sep.join(seq) # 'join' is the inverse of 'split', will print '1+2+3+4+5'

S = 'ABc'
print S.lower() # 'lower' returns a lowercase version of the string

S = 'ababac'
print S.replace('ab', 'c') # 'ab' replaced by 'c'

S = '1+2+3+4+5'
print S.split('+') # split a string into a sequence, default is spaces or tabs or newlines and so on

S = '123ab333cd321'
print S.strip('123') # remove the char in list where on the left and right of the string, default is spaces

