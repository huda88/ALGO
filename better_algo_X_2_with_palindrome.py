__author__ = 'Julia'

def better_algo_X_2(a):
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
    a = []
    for index in range(len(Final)):
        if Final[index]%2 != 0:
            count += 1
            if count >1:
                print(False)
                return False
        if Final[index]%2 == 0 and Final[index] > 0:
            b = Final[index]//2
            if index > 9:
                a.insert(0, [chr(index+54)]*b)
                a.insert(len(a), chr(index+54)*b)
            else:
                a.insert(0, str(index)*b)
                a.insert(len(a), str(index)*b)
        elif Final[index] > 0:
            if index > 9:
                a.insert(len(a)//2, chr(index+54))
            else:
                a.insert(len(a)//2, index)
    b=''
    for index in a:
        b= b+ index
    a=[]
    for index in b:
        a += index

    print(a)
    return True
