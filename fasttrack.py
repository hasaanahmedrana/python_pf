def technicalsupport():
    inp=int(input('number of attempt:'))
    for i in range(inp):
        a=int(input('number of alpha:'))
        b=input('input:')
        score=0
        s=''
        for j in range(a):
            c=b[j]
            length2=len(s)
            for k in range(length2):
                d=s[k]
                if( d=='q' or d=='Q') and (c=='q' or c== 'Q'):
                    print('NO')
                    return
            s=s+c
            print(s)
            if j==(a-1) and ( c=='Q' or c=='q'):
                print('N0')
                return
            if c=='Q'or c=='q':
                score+=1
            if c=='A' or c=='a':
                score-=1
        if score<=0:
            print('YES')
        else:
            print('NO')
technicalsupport()

def gender():
    inp=input('')
    length=len(inp)
    string='_'
    distinct_alpha=0
    for i in range (length):
        length_of_s=len(string) 
        a=inp[i]
       
        for k in range (length_of_s):
            b=string[k]
            count=0
            if b!=a:
                count+=1
            if b==a:
                count=0
                break    
        if count>0: 
            distinct_alpha+=1
        string=string+a
    if distinct_alpha%2==0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')
gender()
gender()
gender()
gender()


luckyticket
def luckeyticket():
    length=int(input(''))
    inp=input('')
    if length%2!=0:
        print('NO')
        return
    else:
        for i in range (length):
            a=inp[i]
            if a!='4' and a!='7':
                print('NO')
                return
    sum1=0
    for j in range (length//2):
        b=int(inp[j])
        sum1+=b
    sum2=0
    for k in range (length//2,length):
        c=int(inp[k])
        sum2+=c
    if sum1==sum2:
        print('YES')
    else:
        print('NO')
luckeyticket()

perfectpermutation
def perfect_permutation():
    n=int(input(''))
    if n==1:
        print('-1')
        return
    if n>1 and n%2==0:
        i=1
        c=1
        while c<=n//2:
            print(i+1,end=' ')
            print(i,end=' ')
            i+=2
            c=c+1
    else:
        print('-1')
perfect_permutation()
def long_words():
    n=int(input(''))
    for i in range(n):
        word=input('')
        length=int(len(word))
        if (length)<=10:
            print(word)
        else:
            print( word[0],end='')
            print(length-2,end='')
            print(word[length-1])  
long_words()

def technical_support():
    num=int(input())
    for i in range(num):
        length=int(input(''))
        inp=input('')
        q=unanswered=0
        for j in range (length):
            a=inp[j]
            if a=='Q' or a=='q':
                q+=1
            else:
                q-=1
            if q<0:
                q=0
        unanswered+=q
        if unanswered==0:
            print('YES')
        else:
            print('NO')
technical_support()

                      

def sum():
    n=int(input(''))
    for i in range(n):
        a,b,c=map(int,input().split())
        if a+b==c or a+c==b or b+c==a:
            print('YES')
        else:
            print('NO')
sum()

def hulk():
    n=int(input(''))
    i=1
    while i <= n:
        if i%2!=0:
            print('I hate',end=' ')
        else:
            print('I love',end=' ')
        if i<n:
            print('that',end=' ')
        if i==n:
            print('it')
        i+=1
hulk()



k=int(input(''))
l=int(input(''))
m=int(input(''))
n=int(input(''))
d=int(input(''))
count=0
for i in range(1,d+1):
    if i%k==0 or i%l==0 or i%m==0 or i%n==0:
        count+=1
print(count)



a,b,n=map(int,input(' ').split())
print(a)
print(b)
print(n)
i==1
while i<=n:
    while n==0:



def elevator():
    n=int(input(''))
    for i in range (n):
        a,b,c=map(int,input('').split())
        if a==1:
            print('1')
        elif b>c:
            if b-1>(a-1):
                print('1')
            elif b-1<(a-1):
                print('2')
            elif b-1==a-1:
                print('3')
        elif b<c:
            x=((c-b)*2)+(b-1)
            if x>(a-1):
                print('1')
            elif x<(a-1):
                print('2')
            elif x==a-1:
                print('3')
        else:
            print('3')
elevator()
            



def increaing():
    n=int(input(''))
    for i in range(n):
        input_length=int(input(''))
        inp=list(map(int,input().split()))
        b=set(inp)
        length_set=len(b)
        if  length_set==input_length:
            print('YES')
        else:
            print('NO')
increaing()


def image():
    n=int(input(''))
    for i in range(n):
        inp1=input('')
        inp2=input('')
        inp=inp1+inp2=q
        s=set(inp)
        print(len(s)-1)
image()


def make_A_equal_B():
    n=int(input(''))
    for i in range (n):
        length=int(input(''))
        array_a=list(map(int,input().split()))
        array_b=list(map(int,input().split()))
        count_1_in_a=count_1_in_b=position_differ=0
        count_1_in_a=array_a.count(1)
        count_1_in_b=array_b.count(1)
        count_differ=abs(count_1_in_a-count_1_in_b)
        for l in range (length):
            if array_a[l]!=array_b[l]:
                position_differ+=1
        if count_1_in_a==count_1_in_b :
            if position_differ==0:
                print('0')
            else:
                print('1')
        elif count_1_in_a!=count_1_in_b:
            if position_differ<=count_differ:
                print(count_differ)
            else:
                print(count_differ+1)
make_A_equal_B()


def epicgame():
    a,b,n=map(int,input().split())
    while n>0:
        i=1
        subtraction=0
        while i<=n:
            if a%i==0 and n%i==0:
                subtraction=i
            i+=1
        n-=subtraction
        if n==0:
            print('0')
            return
        k=1
        subtraction=0
        while k<=n:
            if b%k==0 and n%k==0:
                subtraction=k
            k+=1
        n-=subtraction
        if n==0 :
            print('1')
            return
epicgame()
                

def jumboextracheese():
    testcase=int(input(''))
    for i in range(testcase):
        num_slices=int(input(''))
        maximum_height=0
        sum_base=0
        for j in range(num_slices):
            slice=list(map(int,input().split()))
            y_axis_side=max(slice)
            if y_axis_side>maximum_height:
                maximum_height=y_axis_side
            x_axis_side=min(slice)
            sum_base+=x_axis_side
        min_perimeter=2*(sum_base+maximum_height)
        print(min_perimeter)
jumboextracheese()




def secondrank():
    length=int(input(''))
    l=list(map(int,input().split()))
    length=len(l)
    for j in range (length-1):      #sorting of element
        for i in range(length-1):   
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
    second_max=0
    for i in range (length-2,-2,-1):
        if l[i]!=l[length-1]:
            second_max=l[i]
            break
    if second_max==0:
        print('NO')
    else:
        count=0
        for k in range (length-1):
            if l[k]==second_max:
                count+=1
        print(count)
secondrank()


n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)
scores.remove(max_score)
if len(scores) == 0:
    print("NO")
else:
    second_max_score = max(scores)
    if second_max_score == max_score:
        print("NO")
    else:
        print(second_max_score)

def doctorling():
    inp=input()
    print(inp)
    length=len(inp)
    print(length)
    s=set(inp)
    lengthofs=len(s)
    print(lengthofs)     
    if length%lengthofs==0 or (length-1)% lengthofs==0 or (length+1)% lengthofs==0:
        print('YES')
    else:
        print('NO')    
doctorling()
doctorling()
doctorling()

def secondrank():
    length=int(input(''))
    inp=list(map(int,input().split()))
    length=len(inp)
    maxi=max(inp)
    a=inp.count(maxi)
    for i in range (a):
        inp.remove(maxi)
    if inp==[]:
        print('NO')
    else: 
        maxi2=max(inp)
        print(inp.count(maxi2))
secondrank()

crazy fan
def crazy_fan():
    n,p=map(int,input().split())
    print(p)
    maxpoint=minpoint=0
    for i in range(n):
        x1,x2=map(int,input().split())
        if x1>x2: x1,x2=x2,x1;
        if i==0:
            maxpoint=x2
            minpoint=x1
        if i!=0:
            for k in range (minpoint,maxpoint+1):
                for m in range (x1,x2+1):
                    if x1[m]==

crazy_fan()

def doctorling():
    inp=input()
    l=list(inp)
    print(l)
    length=len(l)
    for i in range (length):
        c=l.count(l[i])
        print(c)
doctorling()
def main():
    n = int(input())
    if n<3: return -1
    if n%7==0: return [0,0,n//7];
    if n%5==0: return [0,n//5,0]
    if n%3==0: return [n//3,0,0] 
    ans=[0,0,0]
    for i in range(3,8,2):
        m = n-i
        if m<3: return -1
        if m%3==0:
            ans[0]=m//3
        elif m%5==0:
            ans[1]=m//5
        elif m%7==0:
            ans[2]=m//7
        if m%3==0 or m%5==0 or m%7==0:
            if i==3: ans[0]+=1;
            if i==5: ans[1]+=1;
            if i==7: ans[2]+=1;
            return ans
    return -1
        
for _  in range(int(input())):
    z = main()
    if z==-1: print(-1);
    else: print(*z)

 if n==8: return '1 1 0'
    if n==10: return '1 0 1'
    if n==12: return '0 1 1'
    five = n//10
    other = n%10
    ans= [0,0,0]
    ans[1]=five*2
    if other%3==0:
        ans[0]=other//3
    if other%5==0:
        ans[1]+=other//5
    if other%7==0:
        ans[2]=other//7
    if sum(ans)==five*2 and other>0: return -1;
    return f'{ans[0]} {ans[1]} {ans[2]}'    