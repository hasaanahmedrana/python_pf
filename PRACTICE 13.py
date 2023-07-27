#task1
f=open('nums.txt','r')
i=1
sum=0
while i <=10000:
    n=int(f.readline())
    sum=sum+n
    i=i+1
average=(sum/10000)
print('Average:',average)
    
#task2
f=open('nums.txt','r')
i=1
count1=count2=count3=count4=count5=0
count6=count8=count7=count9=count10=0
while i <=10000:
    n=int(f.readline())
    if n==1:
        count1=count1+1
    if n==2:
        count2=count2+1
    if n==3:
        count3=count3+1
    if n==4:
        count4=count4+1
    if n==5:
        count5=count5+1
    if n==6:
        count6=count6+1
    if n==7:
        count7=count7+1
    if n==8:
        count8=count8+1
    if n==9:
        count9=count9+1
    if n==10:
        count10=count10+1
    i=i+1
print('Count 1:', count1)
print('Count 2:', count2)
print('Count 3:', count3)
print('Count 4:', count5)
print('Count 5:', count5)
print('Count 6:', count6)
print('Count 7:', count7)
print('Count 8:', count8)
print('Count 9:', count9)

#task3
f=open('nums.txt','r')
i=1
count1=count2=count3=count4=count5=0
count6=count8=count7=count9=count10=0
while i <=10000:
    n=int(f.readline())
    if n==1:
        count1=count1+1
    if n==2:
        count2=count2+1
    if n==3:
        count3=count3+1
    if n==4:
        count4=count4+1
    if n==5:
        count5=count5+1
    if n==6:
        count6=count6+1
    if n==7:
        count7=count7+1
    if n==8:
        count8=count8+1
    if n==9:
        count9=count9+1
    
    i=i+1
f2=open('counts.txt','w')
a=f2.write(f'{str(count1)}\n')
a=f2.write(f'{str(count2)}\n')
a=f2.write(f'{str(count3)}\n')
a=f2.write(f'{str(count4)}\n')
a=f2.write(f'{str(count5)}\n')
a=f2.write(f'{str(count6)}\n')
a=f2.write(f'{str(count7)}\n')
a=f2.write(f'{str(count8)}\n')
a=f2.write(f'{str(count9)}\n')
f2.close()

#task4
f=open('counts.txt','r')
sum=0
i=1
while i <=9:
    n=int(f.readline())
    sum=sum+n
    i=i+1
f.close()
print('SUM:',sum)
#task5
f=open('letters.txt','r')
i=1
A=B=C=D=E=F=G=H=I=J=K=L=M=N=O=P=Q=R=S=T=U=V=W=X=Y=Z=0
while i <=100:
    alpha=(f.readline().strip())
    if alpha=='A':
        A=A+1
    if alpha=='B':
        B=B+1
    if alpha=='C':
        C=C+1
    if alpha=='D':
        D=D+1
    if alpha=='E':
        E=E+1
    if alpha=='F':
        F=F+1
    if alpha=='G':
        G=G+1
    if alpha=='H':
        H=H+1
    if alpha=='I':
        I=I+1
    if alpha=='J':
        J=J+1
    if alpha=='K':
        K=K+1
    if alpha=='L':
        L=L+1
    if alpha=='M':
        M=M+1
    if alpha=='N':
        N=N+1
    if alpha=='O':
        O=O+1
    if alpha=='P':
        P=P+1
    if alpha=='Q':
        Q=Q+1
    if alpha=='R':
        R=R+1
    if alpha=='S':
        S=S+1
    if alpha=='T':
        T=T+1
    if alpha=='U':
        U=U+1
    if alpha=='V':
        V=V+1
    if alpha=='W':
        W=W+1
    if alpha=='X':
        X=X+1
    if alpha=='Y':
        Y=Y+1
    if alpha=='Z':
        Z=Z+1
    i=i+1
f.close()
print('Count of A:',A)
print('Count of B:',B)
print('Count of C:',C)
print('Count of D:',D)
print('Count of E:',E)
print('Count of F:',F)
print('Count of G:',G)
print('Count of H:',H)
print('Count of I:',I)
print('Count of J:',J)
print('Count of K:',K)
print('Count of L:',L)
print('Count of M:',M)
print('Count of N:',N)
print('Count of O:',O)
print('Count of P:',P)
print('Count of Q:',Q)
print('Count of R:',R)
print('Count of S:',S)
print('Count of T:',T)
print('Count of U:',U)
print('Count of V:',V)
print('Count of W:',W)
print('Count of X:',X)
print('Count of Y:',Y)
print('Count of Z:',Z)



