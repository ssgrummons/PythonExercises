#/usr/bin/python
'''
Identify the number of bits set to 1 in A * B.
'''

def solution(A, B):
    product = A * B
    binary = (bin(product)[2:])
    return binary.count('1')

