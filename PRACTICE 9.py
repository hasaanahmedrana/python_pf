#TASK3
number=(input('Enter Three Digitr Number='))
print('First Digit=',number[0])
print('Second Digit=',number[1])
print('Third Digit=',number[2])
#second method using integer division and remainder)
number = int(input("Enter a three-digit number: "))

first_digit = number // 100
second_digit = (number // 10) % 10
third_digit = number % 10

print(first_digit, second_digit, third_digit)
#TASK4
#TASK4
#TASK4
number=(input('Enter Three Digitr Number='))  
FirstDigit=int(number[0])
SecondDigit=int(number[1])
ThirdDigit=int(number[2])
print('Sum=',ThirdDigit+SecondDigit+FirstDigit)

#TASK5
#TASK5
#TASK5
number=(input('Enter Three Digitr Number='))
FirstDigit=(number[0])
SecondDigit=(number[1])
ThirdDigit=(number[2])
print('Reverse=',ThirdDigit+SecondDigit+FirstDigit)
#TASK1
#TASK1
#TASK1
from random import*
n=str(input('Enter Card Type:'))

if n=='d' or n=='h ' or n=='D'or n=='H':
    print('Red')
if n=='s' or n=='S' or n=='c' or n=='C':
    print('Black')

#TASK2
#TASK2
#TASK
from random import*
x= randint(1,13)
y=randint(1,4)
if y==1:
    t1='Diamond'
if y==2:
    t1='Heart'
if y==3:
    t1='Spade'
if y==4:
    t1="Club"
t2=0
if x==1:
    t2='Ace'
if x==11:
    t2='Jack'
if x==12:
    t2='Queen'
if x==13:
    t2='King'
if x==2:
    t2='Two' 
if x==3 :
    t2='Three'
if x==4 :
    t2='Four'
if x==5 :
    t2='Five' 
if x==6 :
    t2='Six'
if x==7 :
    t2='Seven'
if x==8 :
    t2='Eighth'
if x==9:
    t2='Nine'
if x==10 :
    t2='Ten'
print(f'{t2} of {t1}')
#task4
#task4
from random import*
x1= randint(1,13)
y1=randint(1,4)
x2= randint(1,13)
y2=randint(1,4)
if x1 ==x2:
    print('Both the cards have same number.')
else:
    ('Both cards have different number.')
if y1==y2:
    print('Both the cards have same type.')
else:
    ('Both cards have different type.')
if (y1==1 and y2==1) or (y1==2 and y2==2) or (y1==1 and y2==2):
    print('Both cards have same colour.')
if (y1==4 and y2==4) or (y1==3 and y2==3) or (y1==3 and y2==4):
    print('Both the cards have same colour')
else:
    ('Both cards have different colour.')


