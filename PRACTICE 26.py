#TASK-1
from random import *
def main():
    length = randint(5, 15)
    x = [0]*length
    for i in range(length):
        x[i] = randint(0, 100)
        print (x[i], end = ' ')
    for j in range (length-1):
        if x[j]<x[j+1]:
            print(f'{x[j]},{x[j+1]}')
main()

#TASK-2
from random import *
def main():
    length = randint(5, 15)
    x = [0]*length
    y = [0]*length
    for i in range(length):
        x[i] = randint(0, 100)
        print(x[i],end=' ')
    print()
    for i in range(length):
        y[i] = randint(0, 100)
        print(y[i],end=' ')
    print()
    for i in range (length):
        if x[i]>y[i]:
            print(x[i],end=' ')
        else:
            print(y[i],end=' ')
main()

#TASK-3
from random import *
def main():
    length = randint(5, 15)
    x = [0]*length
    y = [0]*length
    print('List 1:',end=' ')
    for i in range(length):
        x[i] = randint(0, 100)
        print(x[i],end=' ')
    print()
    print('List 2:',end=' ')
    for i in range(length):
        y[i] = randint(0, 100)
        print(y[i],end=' ')
    print()
    for i in range (length):
        if x[i]>y[i]:
            x[i],y[i]=y[i],x[i]
    print('List 1:',end=' ')
    for i in range (length):
        print(x[i],end=' ')
    print()
    print('List 2:',end=' ')
    for i in range (length):
        print(y[i],end=' ')
main()

#TASk-4
from random import *
def main():
    length = randint(5, 15)
    x = [0]*length
    a='List is sorted'
    for i in range(length):
        # x[i] = randint(0, 100)
        x[i] = int(input(''))
        print (x[i], end = ' ')
    for j in range(length-1):
        if x[j]>x[j+1]:
            a ='List is not sorted'
            break
    print()
    print(a)
main()
