__author__ = 'Julia'

import sys

A = []

for line in sys.stdin:
    for word in line.strip().split():
        A.append(int(word))

def merge(a):
                     ###
    l = len(a)
    if l == 1:
     return a
    a1 = merge(a[:l//2])
    a2 = merge(a[l//2:])
    a_sort = []
    index1, index2 = 0, 0
    while index1 < len(a1) and index2 < len(a2):

        if str(a1[index1]) >= str(a2[index2]):
            a_sort.append(str(a2[index2]))
            index2 += 1

        else:
            a_sort.append(str(a1[index1]))
            index1 += 1
    if index1 < len(a1):
        a_sort.extend(a1[index1:])
    else:
        a_sort.extend(a2[index2:])
    print(a_sort)
    return a_sort

def better_algo_X(a):
    if len(a) < 1:
        print('error: no input values')
        exit(-1)
    count = 1
    odd = 0
    a_sort = merge(a)
    if len(a)<2:
        return True
    for i in range(0,len(a_sort)):
        if a_sort[i-1] == a_sort[i]:
            count += 1
        elif count % 2 != 0:
            odd += 1
            count = 1
            if odd > 1:
                return False
        else:
            count = 1
    return True

better_algo_X(A)
