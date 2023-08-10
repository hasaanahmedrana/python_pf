#TASK-1
# from random import*
# x=[0]*10
# for i in range(len(x)):
#     x[i]=randint(0,50)
# print(x)
# for i in range (len(x)-1,-1,-1):
#     print(x[i],end=' ')
# print()

# #TASK-2
# from random import*
# x=[0]*10
# sum=0
# for i in range(len(x)):
#     x[i]=randint(0,50)
#     sum+=x[i]
# print(x)
# print('SUM:',sum)
# print()

# #TASK-3
# from random import*
# x=[0]*10
# for i in range(len(x)):
#     x[i]=randint(0,50)
# y=[x[i] for i in range(len(x))]
# print(x)
# # x.remove(x[2])
# # z=x
# # print(z)
# print(x)
# print(y)

# #TASK-4
# from random import*
# length=int(input(''))
# x=[0]*length
# y=[0]*length
# for i in range(length):
#     x[i]=randint(1,50)
#     y[i]=randint(1,50)
# for j in range(length-1):
#     for i in range (length-1):
#         if x[i]>x[i+1]:
#             x[i],x[i+1]=x[i+1],x[i]
#         if y[i]>y[i+1]:
#             y[i],y[i+1]=y[i+1],y[i]
# print(x)
# print(y)
# # (()
# for i in range (length):
#     x.append(y[i])
# print(x)
# for j in range(length*2-1):
#     for i in range (length*2-1):
#         if x[i]>x[i+1]:
#             x[i],x[i+1]=x[i+1],x[i]
# print(x) #))
# #or
# # (((()
# z=[]
# for i in range(length):
#     z.append(x[i])
#     z.append(y[i])
# print(sorted(z))   #)))

# #TASK-5
# from random import*
# length=int(input(''))
# x=[0]*length
# for i in range(length):
#     x[i]=randint(1,50)
# print(f'x={x}')
# print('Even numbers of x: ',end=' ')
# even_count=0
# for i in range(length):
#     if x[i]%2==0:
#         print(x[i],end=' ')
#         even_count+=1
# print()
# print('Odd numbers of x: ',end=' ')
# odd_count=0
# for i in range(length):
#     if x[i]%2!=0:
#         print(x[i],end=' ')
#         odd_count+=1
# print()
# print('Even Count:',even_count)
# print('Odd Count:',odd_count)
# for i in range(length):
#     if odd_count<even_count:
#         if x[i]%2!=0:
#             x[i]=x[i]+1
#     if odd_count>even_count:
#         if x[i]%2==0:
#             x[i]=x[i]-1
# print(f'x={x}')
# print()

# # TASK-6
# from random import *
# length = int(input())
# x = [0] * length
# for i in range(length):
#     if i == 0:
#         x[i] = randint(1, 15)
#     else:
#         x[i] = randint(1, 15)
#         if x[i] in x[:i]:
#             while x[i] in x[:i]:
#                 x[i] = randint(1, 15)
# print(x)
# #or
# from random import *
# x=[ ]
# while (len(x))<=10:
#        num=randint(1,15)
#        if num not in x:
#             x.append(num)
# print(x)


# #wrongone
# from random import *
# length = int(input())
# x = [0] * length
# for i in range(length):
#     if i == 0:
#         x[i] = randint(1, 15)
#     else:
#         n=randint(1,15)
#         for j in range (length):
#             if x[j]==n:
#                 n=randint(1,15)
#         x[i]=n
# print(x)

# from random import*
# length=int(input())
# x=[0]*length
# for i in range(length):
#     if i==0:
#         x[i]=randint(1,15)
#     else:
#         x[i]=randint(1,15)
#         if x[i] in x:
#             while x[i] in x:
#                 x[i]=randint(1,15)
# print(x)


# #TASK-7
# from random import*
# length=int(input(''))
# x=[0]*length
# for i in range(length):
#     x[i]=randint(1,5)
# print(x)
# y=[]
# for i in range(length):
#     if x[i] not in y:
#         y.append(x[i])
# for i in range(len(y)):
#     n=[]
#     for j in range (length):
#         if y[i]==x[j]:
#             n.append(j)
#     print(f'{y[i]} is present at',end=' ')
#     for k in range(len(n)):
#         print(f'{n[k]}',end=' ')
#     print()

#  #0r 

# from random import*
# length=int(input(''))
# x=[0]*length
# for i in range(length):
#     x[i]=randint(1,5)
# print(x)
# set=set(x)
# s=list(set)
# print(s)
# for i in range (len(s)):
#     print(f'{s[i]} is pesent in',end=' ')
#     for k in range(len(x)):
#         if s[i]==x[k]:
#             print(k,end=' ')
#     print('positions.')
#     print()


# #TASK-8
# from random import*
# length=int(input(''))
# x=[0]*length
# for i in range(length):
#     if i==0:
#         x[0]=randint(1,2)
#     else:
#         x[i]=randint(1,2)+x[i-1]
# print(x)

# a=x[0]
# b=x[len(x)-1]
# y=[]
# for i in range(a,b+1):
#     y.append(i)
# print(y)
# for i in range(len(y)):
#     if y[i] not in x:
#         print(y[i],end=' ')



# #TASK-9
# from random import *
# x = [0] *20
# for i in range (len(x)):
#     x[i]=randint(0,9)
#     print(x[i],end=' ')
# print()
# for i in range (2,len(x)-2):
#     x[i]=(x[i-2]+x[i-1]+x[i+1]+x[i+2])//4
# for i in range (len(x)):
#     print(x[i],end=' ')
# print()


# #TASK-10
# from random import*
# x=[0]*10
# for i in range (10):
#     x[i]=randint(3,7)
# print(x)
# for i in range (10):
#     for j in range(x[i]):
#         print('*',end=' ')
#     print()

# #TASK-11
# from random import*
# x=[0]*10
# for i in range (10):
#     x[i]=randint(3,7)
# print(x)
# for i in range(10):
#     for j in range(i+1):
#         print(x[j],end=' ')
#     print()

# #TASK-12
# from random import*
# x=[0]*10
# for i in range (10):
#     x[i]=randint(3,7)
# print(x)
# for i in range(10):
#     sum=0
#     for j in range(i+1):
#         print(x[j],end=' ')
#         sum+=x[j]
#     print("=",sum)
# #     print()

# #TASK-13
# from random import*
# x=[0]*10
# for i in range (10):
#     x[i]=randint(3,7)
# print(x)
# for i in range (10):
#     for j in range(1,10):
#         print(f'{x[j-1]} {x[j]} {x[j+1]}')
#     print()

# # #TASK-14(a)
# from random import*
# x=[[randint(0,9) for i in range (10)]for j in range (10)]
# for i in range (10):
#     for j in range(10):
#         print(x[i][j],end=' ')
#     print()
# for i in range (10):
#     for k in range(i):
#         print(' ',end=' ')
#     print(x[i][i])
# print()
# print()
# #14-b
# for i in range (10):
#     for j in range(10):
#         if x[i][j]==0:
#             x[i][j]=1
#         print(x[i][j],end=' ')
#     print()
# print()
# #TASK-15
# from random import*
# x=[[randint(0,9) for i in range (10)]for j in range (10)]
# for i in range (10):
#     for j in range(10):
#         print(x[i][j],end=' ')
#     print()
# print('INDEXES:')
# for i in range (10):
#     for j in range(10):
#         if x[i][j]==0:
#             print(i,j)
# #TASK-9
from random import*
length=int(input(''))
x=[0]*length
for i in range (length):
    x[i]=randint(0,9)
print(x)
z=[]*20
z[0]=x[0]
z[1]=z[1]
z[length]=x[length]
z[length-1]=z[leng]
sum=0
for i in range (2,length-2):
    z[i]=( x[i+1]+ x[i+2]+x[i-2]+x[i-1])//4
print(z)




