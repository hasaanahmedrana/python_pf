n=int(input('N:'))
for i in range (n):
    for j in range  (i):
        print(end=' ')
    if i <n-1:
        print("*",end='')
    if i==n-1:
        print(" *",end='')
    for m in range (1,2*(n-i)-1+1):
        print(end=' ')
    if i<n-1:
        print('*',end='')
    if i >0:
        for k in range (1,i*2-1+1):
            print(end=' ')
        if i <n-1:
            print('*',end='')
    for l in range(1,2*(n-i)-1+1):
        print(end=' ')
    print('*',end='')
    print()
