#TASK1
a=int(input('Enter value of a='))
b=int(input('Enter value of b='))
c=int(input('Enter value of c='))
disc=(b**2)-4*a*c
rootdisc=disc**0.5
denom=2*a
if a==0:
    print('EQUATION IS LINEAR AND HAVE ONLY ONE ROOT.')
if disc==0:
    print('ROOTS ARE IMAGINARY.')
else:
   print('ROOT1=',(-b+rootdisc)/denom)
   print('ROOT2=', (-b-rootdisc)/denom)
   
#TASK2
from random import*
x=randint(0,10)
print(x)
print('guess the selected number=')
g1=int(input(('guess1=')))
if g1==x:
    print('you win')
else:
         g2=int(input(('guess2=')))
         if g2==x:
            print('you win')
         else:
             print('you win')
             g3=int(input(('guess3=')))
             if g3==x:
                   print('you win')
             else:
                    print('you loose')




print()
print()
#TASK3
#TASK3
from random import*
x=randint(0,10)
y=randint(0,10)
z=randint(0,10)
print(x,y,z)
if abs(x-y)>2 and abs(y-z)>2 and abs(x-z)>2:
    print('OKAY')
else:
    print('SORRY')
print()
print()
print()


#TASK4

from random import*
x1=randint(0,100000)
x2=randint(0,100000)
x3=randint(0,100000)
x4=randint(0,100000)
print (f'({x1}\t{x2}\t{x3}\t{x4})')
max=x1
if x2>max :
    max=x2
if x3>max:
    max=x3
if max<x4:
   max=x4
min=x1
if x1<min:
    min=x1
if x2<min:
    min=x2
if x3<min:
    min=x3
if x4<min:
    min=x4
med1=x1
med1!=max
med1!=min
if x2>min and x2<max:
    med1=x2
if x3>min and x2<max:
    mid1=x3
if x4>min and x3<max:
    mid1=x4
med2=x1
med2!=max
med2!=min
med2!=med1
med2>med1
if x2>min and x2<max and x2>med1:
    med2=x2
if x3>min and x3<max and x3>med1:
    med2=x3
if x4>min and x4<max and x4>med1:
    med2=x4
med2!=med1!=max!=min


print(min,med1,med2, max)