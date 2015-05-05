__author__ = 'Julia'

#This version is the version returning also a palindrome.

import sys

A = []

for line in sys.stdin:
    for word in line.strip().split():
        A.append(int(word))

def better_algo_X(a):

    if len(a) < 1:
        print('error: no input values')
        exit(-1)

    Final=[]
    for i in range(69):
        Final.append(0)
    for i in range(len(a)):
        if type(a[i]) == type('A'):
            Final[ord(a[i])-54] += 1
        else:
            Final[a[i]] += 1
    count = 0
    for index in Final:
        if index%2 != 0:
            count += 1
            if count >1:
                return False
    return True



better_algo_X(A)