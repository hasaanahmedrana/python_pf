# #TASK-1
# x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
# length=len(x)
# y=[]
# for i in range (length-1):
#     if x[i]  not in y:
#         y.append(x[i])
#         print(x[i],end=' ')
# print()

# #or 

# x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
# length=len(x)
# y=set(x)
# y=list(y)
# for i in range(len(y)):
#     print(y[i],end=' ')
# print()

# #TASK-2
# x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
# length=len(x)
# y=[]
# for i in range (length-1):
#     if x[i]  not in y:
#         y.append(x[i])
# print(y)

# #TASK-3
# x = [23, 45, 18, 23, 17, 45, 36, 23, 45, 18, 36, 45, 18, 17, 36, 23, 17]
# length=len(x)
# y=[]
# for i in range (length-1):
#     if x[i]  not in y:
#         y.append(x[i])
# z=[]
# for k in range(len(y)):
#     a=x.count(y[k])
#     z.append(a)
# print(y)
# print(z)

#TASK-4
# from random import*
# row=int(input(''))
# col=int(input(''))
# x=[[randint(10,99) for i in range (col)]for j in range(row)]
# for i in range (row):
#     for j in range (col):
#         print(x[i][j],end=' ')
# print()
# for i in range (row):
#     for j in range (col):
#         print(x[i][j],end=' ')
#     print()
# print()
# for i in range(col):
#     for j in range(row):
#         print(x[j][i],end=' ')
#     print()

# #task-5
# from random import*
# row=int(input(''))
# col=int(input(''))
# x=[[randint(10,99) for i in range (col)]for j in range(row)]
# for i in range (row):
#     for j in range (col):
#         print(x[i][j],end=' ')
# print()
# for i in range (row):
#     for j in range (col):
#         print(x[i][j],end=' ')
#     print()
# print('PRIMARY DIAGONAL:',end=' ')
# for i in range (row):
#     # for j in range (col):
#         print(x[i][i],end=' ')
# print()
# print('SECONDARY DIAGONAL:',end=' ')
# for i in range (1,row+1):
#     # for j in range (col-1,0,-1):
#     print(x[i-1][row-i],end=' ')
# print()
# #TASK-6
# from random import*
# row=int(input(''))
# col=int(input(''))
# x=[[randint(10,99)for i in range (col)]for j in range (row)]
# for i in range (row):
#     for j in range (col):
#         print(x[i][j],end=' ')
# print()
# for i in range (row):
#     for j in range (col):
#         print(x[i][j],end=' ')
#     print()
# for i in range (row):
#     sum=0
#     for j in range (col):
#         print(x[i][j],end=' ')
#         sum+=x[i][j]
#     print(f'= {sum}')
# print()
    
 










    