#TASK-1
#three random numbers in range 1 to 10. Using loop ensure that all of them are different.
from random import*
def main():
    n1=randint(1,10)
    n2=randint(1,10)
    n3=randint(1,10)
    while n1==n2:
        n2=randint(1,10)
    while n2==n3:
        n3=randint(1,10)
    while n1==n3:
        n1=randint(1,10)
    print(n1, n2 ,n3)
main()

#TASK-2
#two random numbers such that second number is multiple of first number
from random import*
def main():
    num1=randint(2,10)
    num2=randint(2,100)
    while num2%num1!=0:
        num2=randint(1,100)
    print(f'N1={num1}\tN2={num2}')
main()

#TASK-3
from random import*
def main():
    num1=randint(1,49)
    num2=randint(1,49)
    count=0
    while (num1+num2!=50):
        num2=randint(1,49)
        count+=1
    print(f'N1={num1}\tN2={num2}\tCount of loop={count}')
main()

#TASK-4
from random import *

def alphabets():
    c1, c2, c3, c4, c5 = randint(65, 90), randint(65, 90), randint(65, 90), randint(65, 90), randint(65, 90)
    while c1 in [65, 69, 73, 79, 85]:
        c1 = randint(65, 90)
    while c2 in [65, 69, 73, 79, 85]:
        c2 = randint(65, 90)
    while c3 in [65, 69, 73, 79, 85]:
        c3 = randint(65, 90)
    while c4 in [65, 69, 73, 79, 85]:
        c4 = randint(65, 90)
    while c5 in [65, 69, 73, 79, 85]:
        c5 = randint(65, 90)
    print(f'{chr(c1)}\t{chr(c2)}\t{chr(c3)}\t{chr(c4)}\t{chr(c5)}')

alphabets()

#TASK-5
from random import*
def main():
    n=randint(1,10)
    for i in range(9):
        print(n)
        a=randint(2,3)
        n+=a
main()

#TASK-6
from random import*
def main():
    for i in range (1,51):
        s=0
        while s < 50 or s>50:
            sum=0
            for j in range(10):
                a=randint(1,10)
                sum+=a
                print(a,end=' ')
            s=sum
            print('sum',s)
            print()
        print(f'-----------{i}-----------')
main() 

#sir solution
from random import *
def main():
    sum1 = 0
    while sum1 != 50:
        value = randint(1, 10)
        sum1 += value
        print (value, end = ' ')
        if sum1 > 50:
            print ()
            sum1 = 0
    print ()
main()


#TASK-7 (pattern)
r=int(input('Row:'))
for i in range(r+1):
    for j in range(i):
        print(end=' ')
    if i==r:
        for j in range(r):
            print('-',end='')
    else:
        print('\ ')
print()
for k in range(r,0,-1):
    for l in range(k-1):
        print(end=' ')
    print('/')

#TASK 9 (pattern)
r=int(input('Row:'))
for i in range (1,(2*r+1)):
    if i==6:
        i=5
    if i<=r:
        for j in range(i-1):
            print('o',end='')
        for k in range (((2*r)-(i-1)*2)):
            print('*',end='')
        for j in range(i-1):
            print('o',end='')
        print()
    if i>r:
        for l in range(2*r-i):
            print('o',end='')
        for m in range((i-r)*2):
            print('*',end='')
        for n in range(2*r-i):
            print('o',end='')
        print()


