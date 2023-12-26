"""
set
dict
string
tuple
list

s = {1,2,3}
print(dir(s))

# add-->set
#this is an example for the add method to set datatype.
s1 = {1,2,3,4}
s1.add(5)
print(s1)
# by using add method we can able to add elements in a set
# s1.add({6,7})
# print(s1)
# it does not take multiple arguments because add method take one element at a time.
# clear --> set
# This is an example of clear method to set datatype
s = {9,8}
s.clear()
print(s)
# it will clear the all the set elements.
# copy --> set
# This is an example for the copy method to set datatype
s1 = {1,2,3}
s2 = s1.copy()
print(s2)
# it will copy the s1 elements into s2

# difference-->set
# This is the example for the difference method to set datatype
s3 = {9,8,7,6}
s4 = {7,6,5,4}
s3_diff_s4 = s3.difference(s4)
print(s3_diff_s4)
# s3_diff_s4 will give the s3 elements which are not present in s4.
s4_diff_s3 = s4.difference(s3)
print(s4_diff_s3)
# s4_diff_s3 will give the s4 elements which are not present in s3.

# difference_update --> set
# This is the example for the difference_update method to set datatype
s5 = {1,2,3,4}
s6 = {3,4,5,6}
s5.difference_update(s6)
print(s5)
# difference_update will modify existing set
# s5 consist of 1,2,3,4
# s6 consist of 3,4,5,6
# s5.difference_update(s6) will return updated s5 with elements which are elements not present in the s6
# o/p will be {1,2}

s7 = {9,7,6,5}
s8 = {1,2,3,4}
s8.difference_update(s7)
print(s8)
# s8.difference_update(s7) will return s8 elements because no common elements are present in s7,s8.

# discard-->set
# this is an example discard method for the set datatype.
s = {1,2,3}
s.discard(1)
print(s)
# s.discard(1) can be remove element 1 in the set s.
s9 = {9,8,7}
s9.discard(4)
print(s9)
#





