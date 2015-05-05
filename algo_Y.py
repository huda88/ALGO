__author__ = 'Julia'


d = [1,2,3,4,5,6,8,10,12,14]
b = [4,6,78,89,67,7,24,31]
a= [34,56,78,120,32,59,12]
c= [234,45,56,67,89,12,90]

def better_algo_Y(A):
    M=[]
    for i in range(len(A)):
        for j in range(i):
            if A[i] < A[j]:
                R = [A[i], A[j]]
            else:
                R = [A[j], A[i]]
            k=0
            while k < len(A):
                if A[k] == R[0] - (R[1]- R[0]):
                    R.insert(0,A[k])
                    k = 0
                elif A[k] == R[-1] + R[-1] -R[-2]:
                    R.append(A[k])
                    k = 0
                else:
                    k += 1
            if len(R) > len(M):
                M =R
    print(M)
    return M

better_algo_Y(d)

better_algo_Y(b)

better_algo_Y(a)

better_algo_Y(c)


