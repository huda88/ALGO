import sys

A=[]
for line in sys.stdin:
    for word in line.strip().split():
        A.append(int(word))

total = 0
mi = A[0]
ma = A[0]

for x in range(len(A)):
    number = (A[x])
    total += number
    if number < mi:
         mi = number
    elif number > ma:
         ma = number


average = float(total) /len(A)

print ("minimum:" , mi, '\n'
       "maximum:" , ma, '\n'
       "average:" , average)