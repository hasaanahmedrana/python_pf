#nested loop(practice 17)
#TASK1
row=int(input('Row:'))
cols=int(input('Coulomn:'))
i=1
while i <= row:
    j=1
    while j<=cols:
        print(f'{i}\t{j}')
        j=j+1
    i=i+1


#TASK(b)
row=int(input('Row:'))
cols=int(input('Coulomn:'))
i=1
while i <=row:
    j=1
    while j <=cols:
        print(j,end=' ')
        j=j+1
    i=i+1
    print()

#TASK(c)
row=int(input('Row:'))
cols=int(input('Coulomn:'))
i=1
while i <= row:
    j=1
    while j <=cols:
        if i==row and j==cols:
            print(f'({i},{j})')
        else:
            print(f'({i},{j})',end=',')
        j=j+1
    i=i+1
#TASK(d)
row=int(input('Row:'))
cols=int(input('Coulomn:'))
i=1
while i <= row:
    n=i
    j=0

    while j < (cols):
        print(n,end=' ')
        n=n+1
        j=j+1
    i=i+1
    print()

#TASK(e)
r=int(input('Row:'))
i=1
while i <= r:
    print(f'\t{i}')
    i+=1

#TASk(f)
row=int(input('Row:'))
i=1
while i <= row:
    j=1
    while j<i:
        print(' ',end='')
        j=j+1
    print(i)

    i=i+1

#task(g)
r=int(input('Row:'))
i=1
while i <=r:
    j=r
    while j > i:
        print(' ',end='')
        j=j-1
    print(i)
    i=i+1
#or

row=int(input('Row:'))
i=1
while i <= row:
    j=0
    while i<(row-j):
        print(' ',end='')
        j=j+1
    print(i)
    i=i+1

#TASK(h)
row=int(input('Row:'))
cols=int(input('Coulomn:'))
i=1
while i <= row:
    j=1
    while j<=cols:
        print(i,end=' ')
        j=j+1
    print()
    i=i+1

#TASK((i)
row=int(input('Row:'))
cols=int(input('Coulomn:'))
i=1
while i <= row:
    j=1
    while j<=cols:
        print(i,end=' ')
        j=j+1
    k=1
    print()
    a=96
    while k<=cols:
        print(chr(i+a),end=' ')
        k=k+1
    print()
    i=i+1



#TASK(j)
row=int(input('Row:'))
cols=int(input('Coulomn:'))
i=1
while i <= row:
    n=i
    j=1
    while j <= (cols):
        print(n,end=' ')
        j=j+1
        n=n+1
    print()
    k=1
    alpha=96
    m=i
    while k <= cols:
            print(chr(alpha+m),end=' ')
            k=k+1
            m=m+1
    i=i+1
    print()






