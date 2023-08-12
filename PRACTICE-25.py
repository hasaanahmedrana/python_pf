# #TASK-1
from random import*
def main():
    length=10
    print('Length:',length)
    list=[0]*10
    sum=0
    for i in range(length):
        list[i]=randint(30,100)
        # list[i]=int(input())
        sum+= list[i]
        print(list[i],end=' ')
    
    print()
    average=sum/10
    print(f'Average:,{average:<2.2f}')
    positive_count=negative_count=0
    for j in range(10):
        x=average-list[j]
        if x>0:
            positive_count+=1
        else:
            negative_count+=1
        print(f'{x:<2.2f}',end=' ')
    print()
    print('Count of positive value:',positive_count)
    print('Count of negative values:',negative_count)
main()



# #TASK-2
from random import*
def main():
    students_no=30
    marks=[0]*students_no
    sum=0
    for i in range(students_no): #all students marks
        marks[i]=randint(1,100)
        # marks[i]=int(input(' '))
        sum+=marks[i]
        print(marks[i],end=' ')
    print()
    average=sum/students_no
    print(f'Average: {average:<2.2f}')
    for i in range(students_no):  #fail students
        if marks[i]<50:
            print(marks[i],end=' ')
    print()
    for i in range(students_no):   #marks above average  
        if marks[i]>average:
            print(marks[i],end=' ')
    print()
    for i in range(students_no):   #marks below average
        if marks[i]<average:
            print(marks[i],end=' ')
main()


#TASK-3
from random import*
def main():
    x=[0]*12
    for i in range (12):
        x[i]=randint(1000,2000)
        # x[i]=int(input(' '))
        print(x[i],end=' ')
    print()
    print('\t Sale in two half')
    first_half=0
    for i in range (6):
        first_half+=x[i]
    print('First Half:',first_half)
    second_half=0
    for i in range (6,12):
        second_half+=x[i]
    print('Second Half:',second_half)
    first_quater=0
    for i in range (3):
        first_quater+=x[i]
    print('\t Quater Wise Sale ')
    print('Sale in Quater 1:',first_quater)
    second_quater=0
    for i in range (3,6):
        second_quater+=x[i]
    print('Sale in Quater 2:',second_quater)
    third_quater=0
    for i in range (6,9):
        third_quater+=x[i]
    print('Sale in Quater 3:',third_quater)
    forth_quater=0
    for i in range (9,12):
        forth_quater+=x[i]
    print('Sale in Quater 4:',forth_quater)
main()





