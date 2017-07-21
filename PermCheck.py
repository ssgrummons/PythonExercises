#/usr/bin/python
'''
Permutation Check
Check to see if a list is a Permutation.
Return 1 if a list containing each integer from 1 to N.
Return 0 if an integer is missing.
'''

def solution(A):
    A.sort()
    length = len(A)
    if length == 0:
        return 0
    a_range = range(length) 
    integers = [x+1 for x in a_range]
    if integers == A:
        return 1
    else:
        return 0

