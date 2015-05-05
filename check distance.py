__author__ = 'Julia'


import sys
b = 0
A = []
k = 0

for line in sys.stdin:
    if line == 0:
        for word in line.strip().split():
            k.append(int(word))
    for word in line.strip().split():
        A.append(int(word))


def merge(a, c):
    global b
    l = len(a)
    if l == 1:
        return a
    a1 = merge(a[:l//2], c)
    a2 = merge(a[l//2:], c)
    a_sort = []
    index1, index2 = 0, 0
    while index1 < len(a1) and index2 < len(a2):
        if a1[index1] >= a2[index2]:
            if (a1[index1]-a2[index2]) < c:
                b = 1
            a_sort.append(a2[index2])
            index2 += 1
        else:
            if (a2[index2]-a1[index1]) < c:
                b = 1
            a_sort.append(a1[index1])
            index1 += 1
    if index1 < len(a1):
        a_sort.extend(a1[index1:])
    else:
        a_sort.extend(a2[index2:])

    return a_sort


def check_duplicate(a, c):
    merge(a, c)
    if b == 0:
        return True
    else:
        return False

check_duplicate(A, k)