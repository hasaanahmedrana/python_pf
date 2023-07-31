#BY WHILE LOOP

#TASK(a)
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
            print(end=' ')
            k+=1
        j+=1
    print()
    i+=1
#TASK(b)
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
#TASK(c)
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
#TASK(d)
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
        if i==n:
            print('*',end='')
        else:
            print('+',end='')
        l+=1
    i+=1
    print()
#TASK(e)
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
#BY FOR LOOP:
#BY FOR LOOP:
#BY FOR LOOP:
#TASK(a)
n=int(input('N:'))
for i in range (1,n+1):
    for j in range (1,1+i):
        print(j,end='')
        for k in range(i):
            print(end=' ')
    print()

#TASK(b)
n=int(input('N:'))
for i in range (1,(2*n-1)+1):
    if i <=n:
        j=i
    else:
        j=2*n-i
    for k in range(1,j+1):
        print('+',end='')
    print()
#TASK (c)
n=int(input('N:'))
for i in range(1,(2*n-1)+1):
    if i <=n:
        c=n-i+1
        s=i-1
    if i>n:
        s=2*n-1-i
        c=i-n+1
    for k in range(1,s+1):
        print(' ',end='')
    for l in range(1,c+1):
        print('+',end='')
    print()
#TASK(d)
n=int(input('N:'))
for i in range(1,(2*n-1)+1):
    if i <=n:
        c=n-i+1
        s=2*i-2
    else:
        c=i-n+1
        s=(n-c)*2
    for j in range(c):
        print('+',end='')
    for k in range(s):
        print(end=' ')
    for l in range(c):
        print('+',end='')
    print()
#TASK(e)
n=int(input('N:'))
r=n-1
c=n+1
for i in range(1,r+1):
    n=0
    for j in range(1,c+1):
        print(chr(97+n),end=' ')
        n+=i
    print()



