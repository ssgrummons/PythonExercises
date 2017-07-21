#/usr/bin/python
'''
Get the length of the constructed list.
You are going to hop, starting at the first item in the array (A[0]), to the index of the value of that item.  
You are then going to continue until you reach a item whose value is -1.
Return the count of the number of hops.
So, if A = [1,4,-1,3,2], return 4 (1,4,2,-1)
'''
def solution(A):
    if len(A) == 0:
        return 0
    if -1 not in A:
        return 0
    if A[0] == 0:
        return 0
    newarray = []
    a_length = len(A)
    newarray.append(A[0])
    for i in newarray:
        if i == -1:
            break
        newarray.append(A[i])
    return len(newarray)

