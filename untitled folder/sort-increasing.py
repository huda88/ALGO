import sys

A=[]
for line in sys.stdin:
    for word in line.strip().split():
        A.append(int(word))

for i in range(len(A)):
    number = i
    while number > 0 and A[number] < A[number-1]:
        A[number], A[number-1] = A[number-1], A[number]
        number -= 1

print("Array in increase order: ", A)