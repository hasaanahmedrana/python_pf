#task 1
#(row=7 , coloums=5)
r=1
while r<=7:
    c=1
    while c<=5:
        print('*',end=' ')
        c=c+1
    print()
    r=r+1

#task2
#take number of rows and coloumns from user
r=int(input('Rows:'))
c=int(input('Coloumns:'))
i=1
while i<=r:
    j=1
    while j<=c:
        print('*',end=' ')
        j=j+1
    print()
    i=i+1
#task3
# input rows and print A to Z in all rows.

rn=int(input('Row numbers:'))
i=1
while i <=rn:
    j=65
    while j <=90:
        print(chr(j),end='')
        j=j+1
    print()
    i=i+1
#task4:
#input rows & columns and print matrix element randomly in range 1-9
from random import*
r=int(input('Rows:'))
c=int(input('Coulomns:'))
i=1
while i <=r:
    j=1
    while j<=c:
        print(randint(1,9),end=' ')
        j=j+1
    print()
    i=i+1
#task5
#input rows print numbers in the pattern
r=int(input('Row:'))
c=r+1
i=1
while i <=r:
    n=i
    j=1
    while j <=c:
        print(n,end= ' ')
        n=n+1
        j=j+1
    print()
    i=i+1
#or
r=int(input('Row:'))
c=r+1
i=1
n=1
while i <=r:
    j=1
    while j<=c:
        print(n,end=' ')
        n=n+1
        j=j+1

    print()
    i=i+1
    n=n-r
