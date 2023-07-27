#TASK1
#(make 10 sets of paired characters by random import and check how many bits are same in each pair)
from random import*
i=1
totalcount=0
while i <=10:
    count=0
    n1=randint(0,256)
    m2=randint(0,256)
    if n1&1== m2&1:
        count=count+1
    if n1&2== m2&2:
        count=count+1
    if n1&4==m2&4:
        count=count+1
    if n1&8== m2&8:
        count=count+1
    if n1&16==m2&16:
        count=count+1
    if n1&32== m2&32:
        count=count+1
    if n1&64== m2&64:
        count=count+1
    if n1&128== m2&128:
        count=count+1
    if n1&256== m2&256:
        count=count+1
    totalcount=totalcount+count
    print(f'{n1} and {m2} have {count} similar bits')
    print('total number of common bits in 10 sets:',totalcount)
    i=i+1
#TASK2
#(DECIMAL TO OCTAL)
decimal=int(input('Enter Decimal Number:'))
string=''
while decimal>0:
    oc=decimal%8
    string=string+str(oc)   #reverse octal
    #string=str(oct)+string  #in sequence octal
    decimal=decimal//8
print((string),end='')
#TASK3
#(GENERATE 10 SETS AND FIND AVERAGE OF EACH , TELL WHICH SET HAVE THE MAX AVERAGE)
from random import*
i=1
maxaverage=0
set=0
while i <=10:
    n1=randint(0,100)
    n2=randint(0,100)
    n3=randint(0,100)
    average=(n1+n2+n3)/3
    print(f'{i}: {n1} {n2} {n3}      {average} ')
    i=i+1
    if maxaverage<average:
        maxaverage=average
        set=i
    print()
print(f'Set Number {set-1}, have the maximum average.')
#TASK4
#(GENERATE 10 SETS AND FIND AVERAGE OF EACH , TELL WHICH SET HAVE THE MAX AVERAGE AND MIN AVERAGE.)
from random import*
i=1
maxaverage=0
minaverage=100

set=0
while i <=10:

    n1=randint(0,100)
    n2=randint(0,100)
    n3=randint(0,100)
    average=(n1+n2+n3)/3
    print(f'{i}: {n1} {n2} {n3}      {average} ')
    i=i+1
    if maxaverage<average:
        maxaverage=average
        set=i
    if minaverage>average:
        minaverage=average
        minset=i
    print()
print(f'Set Number {set-1}, have the maximum average.')
print(f'Set Number {minset-1}, have the minimum average.')
