                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                c c'''n=int(input('N:'))
k=int(input('k:'))
i=1
while i <=n:
    j=1
    while j <= k:
        print(f'{i}\t{j}')

        j=j+1
    i+=1


r=int(input('Row:'))
c=int(input('Coloumn'))
i=1
while i <=r:
    j=1
    while j <=c:
        print(j ,end= ' ')
        j=j+1
    print()
    i=i+1

n=int(input('N:'))
k=int(input('k:'))
i=1
while i <=n:
    j=1
    while j <=c:
        if i==n and j==k:
            print(f'({i},{j})')
        else:
            print(f'({i},{j})',end=',')
        j=j+1
    i+=1
r=int(input('Row:'))
c=int(input('Coloumn:'))
i=1
while i <= r:
    j=1
    n=i
    while j <=c:
        print(n,end=' ')
        n+=1
        j+=1
    print()
    i+=1
r=int(input('Row:'))
i=1
while i <= r:
    print(f'\t{i}')
    i+=1
r=int(input('Row:'))
i=1
while i <=r:
    j=1
    while j < i:
        print(' ',end=' ')
        j=j+1
    print(i)
    i=i+1
r=int(input('Row:'))
i=1
while i <=r:
    j=r
    while j > i:
        print(' ',end='')
        j=j-1
    print(i)
    i=i+1

row=int(input('Row:'))
i=1
while i <= row:
    j=0
    while i<(row-j):
        print(' ',end='')
        j=j+1
    print(i)
    i=i+1
r=int(input('Row:'))
c=int(input('Coulomn:'))
i=1
while i <= r:
    j=1
    while j <= c:
        print(i,end= ' ')
        j+=1
    print()
    i+=1
r=int(input('row:'))
c=int(input('Coulomn:'))
i=1
while i <= r:
    j=1
    while j <=c:
        print(i,end=' ')
        j+=1
    k=1
    print()
    while k <=c:
        print(chr(96+i),end=' ')
        k+=1
    print()
    i=i+1
r=int(input('Row:'))
c=int(input('Coulomn:'))
i=1
while i <=r:
    j=1
    n=i
    while j <=c:
        print(n,end=' ')
        j+=1
        n+=1
    print()
    k=1
    m=i
    while k <=c:
        print(chr(96+m),end=' ')
        k+=1
        m+=1
    print()
    i+=1
#TASK((j)
row=int(input('Row:'))
cols=int(input('Coulomn:'))
i=1
while i <= row:
    j=1
    while j<=cols:
        print(j,end=' ')
        j=j+1
    k=1
    print()
    a=96
    while k<=cols:
        print(chr(k+a),end=' ')
        k=k+1
    print()
    i=i+1
r=int(input('Row:'))
i=1
alpha=65
while i <=r:
    j=1
    while j <= r:
        print(chr(alpha),end=' ')
        alpha+=1
        j+=1
        k=1
        while k <j:
            print(k,end=' ')
            k+=1
    i+=1
n=int(input('N:'))
i=1
while i <=n:
    j=1
    while j<i:
        print(' ',end='')
        j+=1
    if i!=n:
        print('|_')
    else:
        print('|_|')
        k=2*n
        while k>i:
            print(' ',end='')
            k-=1
        print('_|')

    i+=1

s=int(input('N:'))
i=1
while i <=s:
    j=s
    while j >i:
        print(' ',end='')
        j-=1
    k=1
    while k <=i:
        print('*',end='')
        k+=1
    i+=1
    print()

n=int(input('N:'))
i=1
r=1
while i <=n:
    j=n
    while j >i:
        print(' ',end='')
        j-=1
    k=1
    while k<=r:
        print(i,,end='')
        k+=1
    i+=1
    r+=2
    print()
n=int(input('N:'))
i=1
while i <=n:
    j=1
    while j<i:
        print(' ',end='')
        j+=1
    if i!=n:
        print('|_')
    else:
        print('|_|')
    k=2*n-2
    while k>=i:
        print(' ',end='')
        k-=1
    if i!=n:
        print( '_|')


    i+=1

n=int(input('N:'))
i=1
while i <=n:
    j=n
    while j >i:
        print(' ',end='')
        j-=1
    k=1
    while k<=i:
        print(k,end='')
        k+=1
    i+=1
    print()

r=int(input('Row:'))
i=1
while i <=r:
    j=r
    while j >i:
        print(' ',end='')
        j-=1
    n=i
    while n>=1:
        print(n,end='')
        n-=1
    k=2
    while k <=i:
        print(k,end='')
        k+=1
    i+=1
    print()
r=int(input('Row:'))
c=int(input('Coloumn:'))
i=1
while i <=r:
    j=1
    sum=0
    n=0
    while j<=c:
        if i==1:
            if j==c:
                print(f'{n+i}',end='')
            else:
                print(f'{n+i}+',end='')
            sum=sum+(n+i)
        else:
            if j==c:
                print(f'{j+n}',end='')
            else:
                print(f'{j+n}+',end='')
            sum=sum+(j+n)
        j+=1
        n=n+(i-1)
    print('=',sum)
    i+=1

#PRACTICE 16 -QUESTION1 BY FOR LOOP
from random import*
a=randint(3,8)
b=randint(3,8)
print(a)
print(b)
for i in range (a):
    for i in range (b):
        print('*',end='')
    print()
#practice 18 task b(while loop)
n=int(input('N:'))
r=2*n-1
i=1
while i <= r:
    if  i<=n:
        c=i
    else:
        c= 2*n-i
    j=1
    while j <=c:
        print('+',end='')
        j+=1
    print()
    i+=1
##practice 18 task b(for oop)
n=int(input('N:'))
r=2*n-1
for i in range(1,r+1):
    if i<=n:
        c=i
    else:
        c=2*n-i
    for j in range (1,c+1):
        print('+',end='')
    print()

n=int(input('N:'))
row=2*n-1
i=1
while i <= row:
    j=1
    if i<=n:
        col=(n-i)+1
    else:
        col=(i-n)+1
    while j <=col:
        k=1
        if i<=n:
            space=i-1
        else:
            space=(2*n-i-1)
        while k <=space:
            print('',end='')
            k=k+1
        print('+',end='')
        j+=1
    i+=1
    print()
#practice 18 task c
n=int(input('N:'))
row=2*n-1
i=1
while i <= row:
    if i<=n:
        col=(n-i)+1
        space=i-1
    else:
        col=(i-n)+1
        space=(2*n-i-1)
    k=1
    while k <=space:
        print('',end=' ')
        k+=1
    j=1
    while j <=col:
        print('+',end='')
        j+=1
    i+=1
    print()
n=int(input('N:'))
i=1
r=2*n-1
while i <=r:
    j=1
    spaces=i*2-2
    c=n-i+1
    while j<=c:
        print('+',end='')
        j+=1
    k=1
    while k<=spaces:
        print(' ',end='')
        k+=1
    l=1
    while l<=c:
        print('+',end='')
        l+=1
    i=i+1
    print()
#practice 18 task (D)
n=int(input('N:'))
i=1
r=2*n-1
while i <=r:
    if i<=n:
        c=n-i+1
        s=2*i-2
    else:
        c=i-n+1
        s=(n-c)*2
    j=1
    while j<=c:
        print('+',end='')
        j+=1
    k=1
    while k<=s:
        print(' ',end='')
        k+=1
    l=1
    while l<=c:
        print('+',end='')
        l+=1
    i+=1
    print()
#task(3)practie 18
n=int(input('N:'))
r=n-1
c=n+1
i=1
while i <= r:
    j=1
    n=0
    alpha=97
    while j <=c:
        print(chr(alpha+n),end=' ')
        j+=1
        n+=i
    i+=1
    print()
#practice(18 (a))
n=int(input('N:'))
i=1
while i <=n:
    s=i-1
    c=i
    j=1
    while j<=c:
        print(j,end='')

        k=1
        while k <=s:
            print('_',end='')
            k+=1
        j+=1
    print()
    i+=1

n=int(input('N:'))
i=1
while i <=n:
    j=1
    while j<=(i-1):
        print(end=' ')
        j+=1
    if i==n:
        print('|_|',end='')
    else:
        print('|_',end='')
    k=1
    while k<((n-i+1)*2)-2:
        print(end=' ')
        k+=1
    if i<n:
        print('_|')
    i+=1
n=int(input('N:'))
i=1
while i <=n:
    s1=1
    while s1<= i-1:
        print(' ',end='')
        s1=s1+1
    print('*',end='')
    s2=n-i
    while s2>=1:
        print(' ',end='')
        s2=s2-1
    print('*',end='')
    s3=n-i
    while s3>=1:
        print(' ',end='')
        s3=s3-1
    print('*',end='')
    print()
    i+=1


n=int(input('N:'))
for i in range (1,n+1):
    for j in range(n,i,-1):
        print(end='_')
    for k in range  (i,0,-1):
        print(k,end='')
    for m in range(2,i+1):
        print(m,end='')
    print()'''




