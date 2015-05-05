
Q = []

def insert(x, Array):
    global Q
    a = len(Array)//2
    if len(Array) < 1:
        Array.append(x)
    elif len(Array) == 1:
        if x <= Array[0]:
            temp = []
            temp.append(x)
            temp += Array
            Q = temp
        else:
            Array.append(x)
    elif x <= Array[a]:
        return insert(x, Array[0: a-1])
    else:
        return insert(x, Array[a+1: len(Array)])

def add(x):
    global Q
    insert(x, Q)
    print('added', x, Q)

def getmin():
    global Q
    if len(Q)<= 1:
        return Q[0]
    else:
        minimum = Q[0]
        Q = Q[1: len(Q)]
        print('getmin', minimum, Q)
    return minimum

def getmax():
    global Q
    if len(Q)<= 1:
        return Q[0]
    else:
        maximum = Q[len(Q)-1]
        Q = Q[0: len(Q) - 1]
        print('getmax', maximum, Q)
    return maximum
