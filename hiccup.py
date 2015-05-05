__author__ = 'Julia'

array=[1,5,6,7,3,4,5,2,6,9, 10]

import sys

A = []
for line in sys.stdin:
    for word in line.strip().split():
        A.append(int(word))


def partition(A, left, right):
    i = left + 1
    pivot = A[left]
    for j in range(left + 1, right + 1):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    pos = i - 1
    A[left], A[pos] = A[pos], A[left]
    return pos


def quick_sort(A, left, right):
    if left < right:
        pivot_pos = partition(A, left, right)
        print(pivot_pos)
        quick_sort(A, left, pivot_pos - 1)
        quick_sort(A, pivot_pos + 1, right)


def hiccup(A):
    quick_sort(A, 0, len(A)-1)
    middle= len(A)//2
    increasing = A[0:middle]
    decreasing = A[middle: len(A)]
    i = 0
    j = len(decreasing)-1
    pos = 0
    Temp =[]
    while i <= len(increasing) or j >= 0:
        if j == 0:
            Temp.append(decreasing[j])
            break

        elif increasing[i] <= decreasing[j]:
            Temp.append(increasing[i])
            Temp.append(decreasing[j])

        elif increasing[i] > decreasing[j]:
            if decreasing[j] >= A[pos-1]:
                Temp.append(decreasing[j])
                Temp.append(increasing[i])

            else:
                Temp.append(decreasing[j])
                Temp.append(increasing[i])
                Temp[pos], Temp[pos-1] = Temp[pos-1], Temp[pos]
        if i < len(increasing):
            i += 1
        if j >= 0:
            j -= 1
        pos += 2
    A = Temp
    print(A)
    return A


hiccup(array)