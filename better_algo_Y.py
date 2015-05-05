__author__ = 'Julia'

import sys

A = []
for line in sys.stdin:
    for word in line.strip().split():
        A.append(int(word))

def better_algo_Y(A):

    if len(A) < 1:
        print('error: no input values')
        exit(-1)
    M=[]
    for i in range(len(A)-1):
        if A[i] < A[i+1]:
            R = [A[i], A[i+1]]
        else:
            R = [A[i+1], A[i]]
        k=0
        while k < len(A):
            if A[k] == R[0] - (R[1]- R[0]):
                R.insert(0,A[k])
                k=0
            elif A[k] == R[-1] + R[-1] -R[-2]:
                R.append(A[k])
                k=0
            else:
                k += 1
        if len(R) > len(M):
            M =R
    print(M)
    return M


better_algo_Y(A)