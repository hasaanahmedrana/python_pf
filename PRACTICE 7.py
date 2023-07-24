#TASK3
from random import*
x1=randint(0,1000)
x2=(randint(0,10000))
x3=randint(0,1000)
print (f'Numbers are  {x1}\t {x2}\t{x3}')
if x1<=x2<=x3:
    print('Numbers are in order')
else:
    print('Numbers are not in order')
print()
print()
print()
 #TASK4
 #TASK4
 #TASK4
marks1=int(input('ENTER MARKS 1='))
marks2=int(input('ENTER MARKS 2='))

if marks1==marks2:
    print('marks are same.')
grade1=0
if marks1>=85 :
    grade1=1
elif marks1<85 and marks1>=80:
    grade1=2
elif marks1<80 and marks1>=75:
    grade1=3
elif marks1<75 and marks1>=70:
    grade1=4
elif marks1<70 and marks1>=65:
    grade1=5
elif marks1<65 and marks1>=60:
    grade1=6
elif marks1<60 and marks1>=58:
    grade1=7
elif marks1<58 and marks1>=55:
    grade1=8
else:
    grade1=9

grade2=0

if marks2>=85 :
    grade1=1
elif marks2<85 and marks2>=80:
    grade=2
elif marks2<80 and marks2>=75:
    grade2=3
elif marks2<75 and marks2>=70:
    grade2=4
elif marks2<70 and marks2>=65:
    grade2=5
elif marks1<65 and marks2>=60:
    grade2=6
elif marks2<60 and marks2>=58:
    grade2=7
elif marks2<58 and marks2>=55:
    grade2=8
else:
    grade2=9


if  marks1 !=marks2 and grade1==grade2:
    print('Marks are almost same')
if grade1 != grade2:
    print('Marks are different')
print()
print()
print()
 #TASK1
 #TASK1
 #TASK1
from random import*
a=randint(0,1000)
b=randint(0,1000)
c=randint(0,1000)
print(f'numbers before arranging= {a}\t{b}\t{c}')
#a<b<c 
if a<b<c :
    a,b,c=a,b,c
elif c>b>a:
    a,b,c=c,b,a
elif a<b>c and a>c:
    a,b,c= c,a,b
elif a<b>c and a<c:
    a,b,c= a,c,b
elif a<c>b and b<a:
    a,b,c=b,a,c
elif b<a>c and c<b:
    a,b,c=c,b,a
elif b<a>c and c>b:
    a,b,c=b,c,a




 #TASK4
 #TASK4
 #TASK4
from random import*
x1=randint(0,100)
x2=randint(0,100)
x3=randint(0,100)
x4=randint(0,100)
print(f'numbers before arranging= {x1}\t{x2}\t{x3}\t{x4}')
if x1==x2 and x3<x4:
     x1,x2,x3,x4=x1,x2,x3,x4
if x1==x2 and x4<x3:
     x1,x2,x3,x4=x1,x2,x4,x3
if x2==x3 and x1<x4:
     x1,x2,x3,x4=x1,x2,x3,x4
if x2==x3 and x4<x1:
     x1,x2,x3,x4=x4,x2,x3,x1
if x3==x4 and x1<x2:
     x1,x2,x3,x4=x1,x2,x3,x4
if x3==x4 and x2<x1:
     x1,x2,x3,x4=x2,x1,x3,x4z
if x4==x1 and x2<x3:
     x1,x2,x3,x4=x2,x3,x4,x1
if x4==x1 and x3<x2:
     x1,x2,x3,x4=x3,x2,x4,x1
     
if x2<x1>x3>x4 and x2<x4:
     x1,x2,x3,x4=x2,x4,x3,x1
if x2<x1>x3>x4 and x2>x4:
     x1,x2,x3,x4=x4,x3,x2,x1
if x2<x1>x4>x3 and x3>x2:
    x1,x2,x3,x4=x2,x3,x4,x1
if x2<x1>x4>x3 and x3<x2:
    x1,x2,x3,x4=x3,x4,x2,x1
if x1<x2>x3>x4 and x4>x1:
    x1,x2,x3,x4=x1,x4,x3,x2
if x1<x2>x3>x4 and x4<x1:
    x1,x2,x3,x4=x4,x3,x1,x2
if x1<x2>x4>x3 and x3>x1:
     x1,x2,x3,x4=x1,x3,x4,x2
if x1<x2>x4>x3 and x3<x1: 
     x1,x2,x3,x4=x3,x4,x1,x2
if x1<x3>x2>x4 and x4>x1: 
    x1,x2,x3,x4=x1,x4,x2,x3
if x1<x3>x2>x4 and x4<x1:
    x1,x2,x3,x4= x4,x2,x1,x3
if x1<x3>x4>x2 and x1>x2:
     x1,x2,x3,x4=x2,x4,x1,x3
if x1<x3>x4>x2 and x1<x2:
     x1,x2,x3,x4=x1,x2,x4,x3
if x1<x4>x2>x3 and x1>x3:
    x1,x2,x3,x4=x3,x2,x1,x4
if x1<x4>x2>x3 and x1<x3:
    x1,x2,x3,x4=x1,x3,x2,x4
if x1<x4>x3>x2 and x1>x2:
    x1,x2,x3,x4=x2,x3,x1,x4
if x1<x4>x3>x2 and x1<x2:
    x1,x2,x3,x4=x1,x2,x3,x4
print(f'numbers after arranging= {x1}\t{x2}\t{x3}\t{x4}')
print()
print()
print()
 #TASK5
 #TASK5
 #TASK5
print(f'numbers after arranging= {a}\t{b}\t{c}')
x=int(input('Enter number='))
mode2=x%2
mode3=x%3
mode5=x%5
mode7=x%7
if mode2==0 and mode3!=0 and mode5!=0 and mode7!=0:
    print('number is divisible by 2')
if mode2!=0 and mode3==0 and mode5!=0 and mode7!=0:
    print('number is divisible by 3')
if mode2!=0 and mode3!=0 and mode5==0 and mode7!=0:
    print('number is divisible by 5')
if mode2!=0 and mode3!=0 and mode5!=0 and mode7==0:
    print('number is divisible by 7')
if mode2==0 and mode3==0 and mode5!=0 and mode7!=0:
 print('number is divisible by 2,3')
if mode2==0 and mode3!=0 and mode5==0 and mode7!=0:
    print('number is divisible by 2,5')
if mode2==0 and mode3!=0 and mode5!=0 and mode7==0:
    print('number is divisible by 2,7')
if mode2!=0 and mode3==0 and mode5==0 and mode7!=0:
    print('number is divisible by 3,5')
if mode2!=0 and mode3==0 and mode5!=0 and mode7==0:
    print('number is divisible by 3,7')
if mode2!=0 and mode3!=0 and mode5==0 and mode7==0:
    print('number is divisible by 5,7')
if mode2==0 and mode3==0 and mode5==0 and mode7==0:
    print('number is divisible by 2,3,5,7')
if mode2==0 and mode3==0 and mode5==0 and mode7!=0:
     print('number is divisible by 2,3,5')
if mode2!=0 and mode3==0 and mode5==0 and mode7==0:
     print('number is divisible by 3,5,7')
