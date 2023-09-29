#PRACTICE 25
from random import randint
length=int(input(''))
x=[0]*length
sum=0
print('Length:',length)
for i in range(length):
    x[i]=randint(1,40)
    print(x[i],end=' ')
    sum+=x[i]
print()
average=sum/length
print("Average:",average)
count_positive=0
for j in range (length):
    x[j]=average-x[j]
    print(x[j],end=' ')
    if x[j]>0:
        count_positive+=1
print()
print("Count of positive number:",count_positive)
print('Count of negative number :',length-count_positive)


from random import randint
length=int(input(''))
x=[0]*length
sum_pass=0
count_pass=0
for i in range (length):        #printing all students number
    x[i]=randint(1,100)
    print(x[i],end=' ')
    if x[i]>=50:
        sum_pass+=x[i]
        count_pass+=1
print()
average=sum_pass/count_pass
print(f'Average:{average:<2.2f}')       #average of pass students
for i in range(length):          #all fail student numbers
    if x[i]<50:
        print(x[i],end=' ')
print()
for i in range (length):          #student with marks above average
    if x[i]>average:
        print(x[i],end=' ')
print()
for i in range (length):          #student with marks below average
    if x[i]<average:
        print(x[i],end=' ')


from random import randint
x=[0]*12
sum_of_first_half=0
sum_of_second_half=0
for i in range(12):
    x[i]=randint(1000,2000)
    print(x[i],end=' ')
    if i<6:
        sum_of_first_half+=x[i]
    else:
        sum_of_second_half+=x[i]
print()
print('Difference of first and second half:',abs(sum_of_first_half-sum_of_second_half))
sum_quater_one=0
sum_quater_two=0
sum_qauter_third=0
sum_quater_four=0
for i in range (12):
    if i <3:
        sum_quater_one+=x[i]
    elif i>=3 and i <6:
        sum_quater_two+=x[i]
    elif i>=6 and i <9:
        sum_qauter_third+=x[i]
    else:
        sum_quater_four+=x[i]
print(sum_of_first_half)
print(sum_of_second_half)
print(sum_quater_one)
print(sum_quater_two)
print(sum_qauter_third)
print(sum_quater_four)



#PRACTICE 26


from random import randint
length=randint(5,9)
x=[0]*length
for i in range(length):
    x[i]=randint(1,30)
    print(x[i],end=' ')
print()
a=1
for i in range(length-1):
    if x[i]>x[i]:
        a+=1
if i ==1:
    print('List is Sorted')
else:
    print('List is not Sorted')

from random import randint
def main():
    a='list is sorted'
    length=randint(4,9)
    x=[0]*length
    for i in range (length):
        x[i]=randint(1,30)
        print(x[i],end='  ')
    print()
    for i in range (length-1):
        if x[i]>x[i+1]:
            a='list is not sorted'
            print(a)
            return
    print(a)
main()

from random import*
length=randint(3,9)
x=[0]*length
for i in range (length):
    x[i]=randint(5,20)
    print(x[i],end='  ')
print()
print('PAIRS IN ORDER:')
for i in range(length-1):
    if x[i]<x[i+1]:
        print(f'{x[i]} , {x[i+1]}')


from random import randint
length=randint(3,10)
x=[0]*length
y=[0]*length
print('List 1:',end=' ')
for i in range (length):
    x[i]=randint(1,30)
    print(x[i],end=' ')
print()
print('List 2:',end=' ')
for i in range (length):
    y[i]=randint(1,30)
    print(y[i],end=' ')
print()
for i in range (length):
    if x[i]<y[i]:
        print(x[i],end=' ')
    else:
        print(y[i],end=' ')

from random import randint
length = randint(3,10)
x=[0]*10
y=[0]*10
print('List 1:',end=' ')
for i in range (length):
    x[i]=randint(10,30)
    print(x[i],end=' ')
print()
print('List 2:',end=' ')
for j in range (length):
    y[j]=randint(10,30)
    print(y[j],end=' ')
print()
print('Smaller:')
for i in range (length):
    if x[i]>y[i]:  x[i],y[i]=y[i],x[i];
    print(x[i],end=' ')
print()
print('Larger:',end=' ')
for i in range (length):
    print(y[i],end=' ')


#PRACTICE 27


x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
print(x)
sentinal=-1
for i in range (len(x)):
    if x[i]!=sentinal:
        print(x[i],end=' ')
    for j in range (i+1,len(x)):
        if x[j]==x[i]:
            x[j]=sentinal

y=[]
c=[]
for i in range (len(x)):
    if x[i] not in y:
        y.append(x[i])
        count=0
        for  j in range (len(x)):
            if x[j]==x[i]:
                count+=1
        c.append(count)

print('X:',end=' ')
for i in range (len(x)):
    print(x[i],end=' ')
print()
print('Y:',end=' ')
for i in range (len(y)):     print(y[i],end=' ');
print()
print('C:',end=' ')
for i in range (len(c)):  print(c[i],end=' ');


from random import randint
r=4
c=3
x=[[randint(2,20)for i in range (c)] for j in range (r)]
print()
for i in range (r):
    for j in range (c):
        print(x[i][j],end=' ')
print()
print()
for i in range (r):
    for j in range (c):
        print(x[i][j],end=' ')
    print()
print()
for i in range (c):
    for j in range (r):
        print(x[j][i],end=' ')
    print()


from random import randint
r=c=4
x=[[randint(10,50)for i in range (r)]for j in range (c)]
for i in range (r):
    for j in range (c):
        print(x[i][j],end=' ')
    print()
print('Primary Diagonal:',end=' ')
for i in range (r):
    print(x[i][i],end=' ')
print()
print('Secondary Diagonal:',end=' ')
for i in range (r):
    print(x[i][r-i-1],end=' ')
    #or
print()
print('Secondary Diagonal:',end=' ')
for i in range (1,r+1):
    print(x[i-1][r-i],end=' ')

r=4
c=3
from random import randint
x=[[randint(10,40)for i in range (c)] for j in range (r)]
for i in range (r):
    sum=0
    for j in range (c):
        print(x[i][j],end=' ')
        sum+=x[i][j]
    print(f' = {sum}')


from random import randint
x=[0]*10
for i in range (10):
    x[i]=randint(1,20)
for j in range (10):
    print(x[j],end=' ')
print()
for j in range (10-1,-1,-1):
    print(x[j],end=' ')


from random import randint
x=[0]*10
for i in range (10):
    x[i]=randint(1,20)
y=[x[i] for i in range (len(x))]
print(x)
print(y)

from random import randint
x=[0]*5
y=[0]*5
for i in range (5):
    if i==0:
        x[i]=randint(1,3)
        y[i]=randint(4,6)
    else:
        x[i]=x[i-1]+randint(1,5)
        y[i]=y[i-1]+randint(1,5)
print(x)
print(y)
z=[]
for i in range (5):
    z.append(x[i])
    z.append(y[i])
for i in range (len(z)-1):
    for j in range (len(z)-1):
        if z[j]>z[j+1]:
            z[j],z[j+1]=z[j+1],z[j]
print(z)
print(sorted(z))


from random import randint
x=[]
while len(x) != 10:
    n=randint(1,15)
    if n not in x:
        x.append(n)
print(x)


from random import randint
x=[0]*10
print('X:',end=' ')
for i in range (10):
    x[i]=randint(1,5)
    print(x[i],end=' ')
print()
y=[]
for i in range (10):         #to get all the  distinct elements of x so  that no repetion in index writing
    if x[i] not in y:
        y.append(x[i])
print()
for i in range(len(y)):
    print(f'INDEX OF {y[i]} in x are :',end=' ')
    for j in range (10):
        if x[j]==y[i]:
            print(j,end=' ')
    print()


from random import randint
x=[0]*20
for i in range (20):
    if i==0:
        x[i]=randint(1,2)
        print(x[i],end=' ')
    else:
        x[i]=randint(1,3)+x[i-1]
        print(x[i],end=' ')
print()
start=x[0]
end=x[len(x)-1]
for i in range (start,end+1):
    if i not in x:
        print(i,end=' ')



from random import randint
# x=[0]*20
x=[3, 2, 0, 1, 2, 4, 6, 2, 1, 9, 8, 2, 3, 4, 6, 2, 0, 1, 3, 4]
for i in range (20):
    # x[i]=randint(0,9)
    print(x[i],end=' ')
for j in range (2,len(x)-3):
    x[j]=(x[j-2]+x[j-1]+x[j+1]+x[j+2])//4
print()
for i in range (20):
    print(x[i],end=' ')


#TASK-13
from random import*
x=[0]*10
for i in range (10):
    x[i]=randint(3,7)
print(x)
for i in range (len(x)-2):
    print(f'{x[i]} {x[i+1]} {x[i+2]}')


file=open("marak.txt","r")
classes=int(file.readline())
maxi=0
for i in range (classes):
    sum=0
    students=int(file.readline())
    for j in range (students):
        marks=int(file.readline())
        sum=sum+int(marks)
    average=sum/students
    if i==0:
        mini=average
        p_min=i
    if average >maxi:
        maxi=average
        p_max=i
    if average <mini:
        mini=average
        p_min=i
print(f'{p_max+1} have maximum average {maxi:<2.2f}')
print(f'{p_min+1} have minimum average {mini}')
file.close()



file1=open("marak.txt","r")
file2=open("abc.txt",'w')
classes=int(file1.readline())
file2.write(str(classes))
file2.write('\n')
for i in range (classes):
    students=int(file1.readline())
    file2.write(str(students))
    file2.write('\n')
    for j in range (students):
        marks=int(file1.readline())
        file2.write(str(marks)+' ')
    file2.write('\n')
file2.close()
file1.close()



from random import *
def main():
    file = open("m2.txt", "w")
    rows = randint(4,8)
    cols = randint(4,8)
    file.write(f'{rows}\n{cols}\n')
    for i in range(rows):
        for j in range(cols):
            value = randint(1, 9)
            file.write(f'{value}')
        file.write('\n')
    file.close()
	
main()


from random import randint
x=[[randint(0,1) for i in range(8)]for j in range(8)]
x[0][0]=1
for i in range (8):
    for j in range (8):
        print(x[i][j],end=' ')
    print()
i=0
j=0
while True:
    print(f'{i},{j}',end=' ')
    if i!=7 and j!=7:
        print('-',end=' ')
    if j+1<7 and x[i][j+1]==1:
        j+=1
    elif i+1<7 and x[i+1][j]==1:
        i+=1
    else:
        break
if i!=7 and j!=7 :
    print('path blocked')
else:
    print(' ')
