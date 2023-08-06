#TASK-1
print('_________TASK-A_____________')
row=int(input('Row:'))
col=int(input('Coloumn:'))
#first line
for i in range (row-2):
    print(end=' ')
for j in range (col):
    print('*',end=' ')
print()
#middle portion
for i in range (row-2,1,-1):
    for j in range (i-1):
        print(end=' ')
    print(end='*')
    for i in range (col*2-3):
        print(end=' ')
    print('*')
#last line
for i in range (col):
    print('*',end=' ')
print()


# # #TASK-2
# print('_________TASK-B_____________')
# print()
# row=int(input('Row:'))
# col=int(input('Coloumn:'))
# for i in range (row):
#     for j in range (col):
#         print(end=' ')
#     print("+")
# for i in range(2*col+1):
#     print(end='+')
# print() 
# for i in range (row):
#     for j in range (col):
#         print(end=' ')
#     print("+")

#TASK-d
count=int(input('count:'))
for i in range (1,count+1):
    if i %2!=0:
        for j in range (1,i+1):
            if j%2!=0:
                print('*',end='')
            else:
                print(end=' ')
        print()
    else:
        for j in range (1,i+1):
            if j%2==0:
                print('*',end='')
            else:
                print(end=' ')
        print()
for i in range (count-1,-1,-1):
    if i %2!=0:
        for j in range (1,i+1):
            if j%2!=0:
                print('*',end='')
            else:
                print(end=' ')
        print()
    else:
        for j in range (1,i+1):
            if j%2==0:
                print('*',end='')
            else:
                print(end=' ')
        print()

# #TASK-E
# row=int(input('Row:'))
# col=int(input('Coloumn:'))
# for i in range (row):
#     for j in range (i):
#         print(end='  ')
#     for k in range (col):
#         print(end='* ')
#     print()


#TASK-F
# from random import randint
# x=[0]*10
# for i in range (len(x)):
#     x[i]=randint(1,30)
# print(x)
# # print(x[:])
# # print(x[2:5])
# y=[0]*10
# for i in range (len(y)):
#     y[i]=randint(1,30)
# print(y)
# x.extend(y)
# print(x)



# from random import uniform
# a=uniform(1,8)
# print(a)
# a=input('Enter names of all person seperated by comma:').split(",")
# print(a)
# import random
# b=random.choices(a,k=2)
# print(f'{b} will pay the bill')


l=['1','2','3']
l2=['5','9','21']
l.append(l2)
print(l[3][2])