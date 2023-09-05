
#TASK-1(a)
print('----------------------TASSK 1(A)------------------------')
from random import randint
length = randint(5,9)
d = [[randint(1,9) for i in range(length)] for j in range(length)]
for i in range(length):
	d[i][i] = 0
for i in range (length):
	for j in range (length):
		print(d[i][j],end=' ')
	print()
city1=int(input('City#1:'))
city2=int(input('City#2:'))
if city2==city1:
    while city2==city1:
        city2=randint(0,length)
print(f'Distance bewteen City {city1} and City {city2}.')
print('Direct distance = ',end=' ')
print(d[city1][city2])
print('Indirect Distances :')
for i in range (length-1):
	if  i!=city1  and i !=city2:
		print(f'Via  City {i+1} distance is :{d[city1][i]+d[i][city2]}')
                


#TASK-1(b)
print('----------------------TASSK 1(B)------------------------')
def shortest(d,city1,city2):
    distance=d[city1][city2]
    via=1
    for i in range(len(d)):
        if i!=city1 and i!=city2:
            indirect_distance=d[city1][i]+d[i][city2]   
            if distance>indirect_distance:
                distance=indirect_distance
                via=i
    if via==city1:
        print(f'Shortest distance between city {city1 + 1} and city {city2 + 1} is {distance}.')
    else:
        print(f'Shortest distance between city {city1 + 1} and city {city2 + 1} is {distance} via {via + 1}.')
from random import*
def main():
    length=randint(3,9)
    d=[[(randint (0,9))for i in range (length)]for j in range (length)]
    for i in range(length):
        d[i][i]=0
    for i in range(length):
        for j in range (length):
            print(d[i][j],end=' ')
        print()
    for i in range(length-1):
        city1 = i
        for k in range(length-1):
            if k != i:
                city2 = k
                shortest(d, city1, city2)
main()
 



#TASK-1(c)
print('----------------------TASSK 1(C)------------------------')
from random import*
def main():
    length=randint(3,9)
    d=[[(randint (1,20))for i in range (length)]for j in range (length)]
    for i in range(length):
        d[i][i]=0
    for i in range(length):
        for j in range (length):
            print(d[i][j],end=' ')
        print()
    for i in range(length):
        city1 = i
        for k in range(length):
            if k != i:
                city2 = k
                if i==0 and k==1:
                    small_distance=d[city1][city2]
                    x=i
                    y=k
                else:
                    distance=d[i][k]
                    if distance<small_distance:
                        small_distance=distance
                        x=i
                        y=k
    print(f'City {x+1} and City {y+1} have the shortest distance {small_distance}')
main()




#TASK 2(a)
print('----------------------TASSK 2(A)------------------------')
from random import randint
def main():
    length=randint(3,9)
    d=[[(randint(1,9))for i in range (length)] for j in range (length)]
    for i in range (length):
        d[i][i]=0
    x=randint(3,length)
    for i in range (x):
        d[randint(0,length-1)][randint(0,length-1)]=-1
    for i in range (length):
        for j in range(length):
            print(d[i][j],end=' ')
        print()
    for i in range (length):
        print(f'City {i} have direct distance with:',end=' ')
        for j in range (length):
            if j !=i:
                distance=d[i][j]
                if distance!=-1:
                    print(j,end=' ')
        print()
main()



#TASK-2(b)
print('----------------------TASSK 2(B)------------------------')
def indirect_distance(d,i,j):
    for k in range (len(d)):
        if k != i and k != j and d[i][k]!=-1 and d[k][j] !=-1:
            print(f'City {i} and {j} have indirect link  via {k}')
            break

from random import randint
def main():
    length=randint(3,9)
    d=[[(randint(1,9))for i in range (length)] for j in range (length)]
    for i in range (length):
        d[i][i]=0
    x=randint(3,length)
    for i in range (x):
        d[randint(0,length-1)][randint(0,length-1)]=-1
    for i in range (length):
        for j in range(length):
            print(d[i][j],end=' ')
        print()
    for i in range (length):
        for j in range (length):
            if j !=i:
                distance=d[i][j]
                if distance==-1:
                    indirect_distance(d,i,j)
main()

