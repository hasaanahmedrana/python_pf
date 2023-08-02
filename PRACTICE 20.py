#TASK-1
# 1(a):
#rectangular box according to rows and columns
def creating_rectangle(r,c):
    i=1
    while i <=r:
        if i==1 or i==r:
            j=1
            while j<=c:
                print('*',end='')
                j+=1  
        else:
            print('*',end='')
            k=1
            while k<= c-2:
                print(end=' ')
                k+=1
            print('*',end='')
        i+=1
        print()
    return

# 1(b):
#print k multiples of n
def k_multiple_of_n(n,k):
    i=1
    while i <=k:
        product=i*n
        print(product ,end=' ') 
        i+=1
    return

# 1(c):
#print n random values in range a to b
from random import*
def n_numbers_in_range(n,a,b):
    i=1
    while i<=n:
        print(randint(a,b),end=' ')
        i+=1
    return

# 1(d):
#finding quadratic root:
def quadraticroots(a,b,c):
    underroot=((b**2)-(4*a*c))**0.5
    root1=(-b+underroot)/(2*a)
    root2=(-b-underroot)/(2*a)
    print(f'x1={root1},x2= {root2}')
    return

#TASK-2
# 2(a):
def middle_value(a,b,c):
    if a<b<c or a>b>c:
       mid=b
    if b<a<c or b>a>c:
        mid=a
    if a>c>b or a<c<b:
        mid=c
    

    return mid

# 2(b):
def average_value(a,b,c):
    add=a+b+c
    average=add/3
    return average
# 2(c):
def x_power_y(x,y):
    result=x**y
    return result

# 2(d):
def next_vowel(c):
    asc=ord(c)
    if asc<69:
        vowel='e'
    elif asc<73:
        vowel='i'
    elif asc<79:
        vowel='o'
    elif asc <85:
        vowel='u'
    elif asc>85 and asc<=90:
        vowel='a'
    return vowel














        



        
