def main():
    r=int(input('Enter no rows: '))
    o=r
    i=1
    while i<=r:
        j=1
        while j<=o:
            print('+',end='')
            j=j+1
        k=1
        if k<i:
            while k<i:
                print(' ',end='')
                k=k+1
            l=1 
            while l<i:
                print(' ',end='')
                l=l+1
        m=1
        if i==r:
            print('*',end='')
        else:
            while m<=o:
             print('+',end='')
             m=m+1
        o=o-1
        i=i+1
        print()
    f=r-2
    a=1
    while a<=r-1:
        b=1
        while b<=a+1:
            print('+',end='')
            b=b+1
        c=1
        while c<=f:
            print(' ',end='')
            c=c+1
        d=1
        while d<=f:
            print(' ',end='')
            d=d+1
        e=1
        while e<=a+1:
            print('+',end='')
            e=e+1
        f=f-1    
        a=a+1
        print()
main()





























main()
