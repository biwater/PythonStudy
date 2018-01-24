# -*- coding: utf-8 -*-
'''
def findMinAndMax(L):
    for i,value in enumerate(L):
        print(value)
        if i == 0:
            minNumber = value
            maxNumber = value
        else:
            if value > maxNumber:
                maxNumber = value
            if value < minNumber:
                minNumber = value
    return (minNumber,maxNumber)

L = [1,2,3,4,5]

t = findMinAndMax(L)
print(t[0])
'''
'''
L = []
for x in range(1,11):
    L.append(x*x)
print(L)
'''
def triangles(x):
    L = [1]
    S = [1]
    k = 0
    while k < x:
        if k == 0:
            pass
        else:
            L.append(0)
            S.insert(0,0)
            for i,value in enumerate(L):
                L[i] = L[i]+S[i]
                S[i] = L[i]

        k = k + 1
        yield L
           

for L in triangles(7):
    print(L)
