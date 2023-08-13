#TASK-1
from random import randint
size=int(input('size:'))
a=[[randint(0,1)for i in range (size)]for j in range (size)]
a[0][0]=1
for i in range (size):
    for j in range (size):
        print(a[i][j],end=' ')
    print()

i=0
j=0
while True:
    print(f'{i},{j}',end=' ')
    if i!=size-1 and j!=size-1:
        print('|',end=' ')
    if j+1<size-1 and a[i][j+1]==1:
        j+=1
    elif i+1<size-1 and a[i+1][j]==1:
        i+=1
    else:
        break
if i!=size-1 and j !=size-1:
    print('Path blocked')
else:
    print()



#TASK-2
size=int(input('size:'))
x=[[randint(1,9)for i in range (size)]for j in range (size)]
for i in range (size):
    for j in range (size):
        print(x[i][j],end=' ')
    print()
for i in range (1,size-1):
    for j in range (1,size-1):
        if i!=size-1 and i != 0 and j!=0 and j !=size-1:
            x[i][j]=(x[i][j+1]+x[i][j-1]+x[i-1][j-1]+x[i-1][j]+x[i-1][j+1]+x[i+1][j-1]+x[i+1][j]+x[i+1][j+1])//8

print('-----------------------')
for i in range (size):
    for j in range (size):
        print(x[i][j],end=' ')
    print()


