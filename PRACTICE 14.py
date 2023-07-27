#TASK1
#(integers divisible by 3 under 100)
i=0
while i<=100:
    i=1+i
    if i %3==0:
        print((i),end=' ')

print()
print('---------------------')
#TASK2
#(integers divisible by 3 and  5 under 100)
i=0
while i<=100:
    i=1+i
    if i %3==0 or i %5==0:
        print((i),end=' ')
print()
print('---------------------')
#TASK3
#(integers divisible by 3 or  5 ,not by both ,under 100)
i=0
while i<=100:
    i=1+i
    if (i%3==0 and i%5!=0)or (i%3!=0 and i%5==0):
        print((i),end=' ')
print()
print('---------------------')
#TASK4
#(take 2 numbers as input, print numbers from smaller to capital and also sum at last)
n1=int(input('ENTER NUMBER1='))
n2=int(input('ENTER NUMBER2='))
if n1<n2:
    i=1
    sum=0
    while n1<=n2:
        print(n1,end=' ')
        sum=sum+n1
        n1=n1+1
        i=i+1
    print()
    print('sum=',sum)

else:
    i=0
    sum=0
    while n1>=n2:
        print(n1,end=' ')
        sum=sum+n1
        n1=n1-1
        i=i+1
    print()
    print('sum=',sum)
print()
print('---------------------')
#TASK5
#(print firsrt hundred integers ,5 in each line )
i=1
j=1
while i<=100 and j<=5:
    print(i,end=' ')
    i=i+1
    j=j+1
    if j==6:
        print()
        j=1

print()
print('---------------------')
#TASK6
#(print alphabets such that vowels should be in different lines from consonents)
i=0
a=65
while i <=25:

    if (a+i==65)or(a+i==68)or(a+i==69)or (a+i==72)or(a+i==73)or(a+i==78)or(a+i==79)or(a+i==84)or(a+i==85):
        print((chr(a+i)),end=' ')
        print()
        i=i+1
    else:
        print((chr(i+a)),end=' ')
        i=i+1


