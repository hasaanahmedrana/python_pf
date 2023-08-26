#TASK-1
def main():
    i=1
    while i<100:
        
        if i<10:
            print(f'[{i}]',end=" ")
        if i>=10:
            a=str(i)
            sum=(int(a[0]))+(int(a[1]))
            if sum<10:
               print(f'[{i} {sum}]',end=' ')
            elif sum>=10:
                b=str(sum)
                sum2=(int(b[0]))+(int(b[1]))
                print(f'[{i} {sum} {sum2}],',end=' ')
        i=i+1
main()
#TASK2
print()
def main():
    i=0
    while i<100:
       i=i+1
       a=i//10
       b=i%10
       if a>=10 and b<=20:
          if a==0 and b==1:
            c='One'
          elif a==0 and b==2:
               c='Two'
          elif a==0 and b==3:
                c='Three'
          elif a==0 and b==4:
                c='Four'
          elif a==0 and b==5:
                c='Five'
          elif a==0 and b==6:
               c='Six'
          elif a==0 and b==7:
               c='Seven'
          elif a==0  and b==8:
               c='Eight'
          elif a==0 and b==9:
               c='Nine'
          elif a==1 and b==0:
                c='Ten'
          elif a==1 and b==1:
               c='Eleven'
          elif a==1 and b==2:
               c='Twelve'
          elif a==1 and b==3:
               c='Thirteen'
          elif a==1 and b==4:
              c='Fourteen'
          elif a==1 and b==5:
              c='Fifteen'
          elif a==1 and b==6:
              c='Sixteen'
          elif a==1 and b==7:
              c='Seventeen'
          elif a==1 and b==8:
              c='Eighteen'
          elif a==1 and b==9:
              c='Ninteen'
       else:
            if a==2:
             a='Twenty'
            if a==3:
             a='Thirty'
            if a==4:
             a='Forty'
            if a==5:
             a='Fifty'
            if a==6:
               'sixty'
            if a==7:
               c='seventy'
            if a==8:
               c='eighty'
            if a==9:
                c='Ninty'
            
main() 
#TASK3
from random import*
def main():
    
    i=0
    marks1 =0

    while i<2:
        i=i+1
        x=randint(0,10)
        y=randint(0,10)
        print('num1=',x )
        print ('num2=',y)
        sum=x+y
        diff=x-y
        product=x*y
        s1=int(input('SUM='))
        d1=int(input('DIFFERENCE=')) 
        p1=int(input('PRODUCT='))
        if (s1==sum) and (d1==diff) and (p1==product):
            marks1=marks1+3
        elif (s1==sum) and (d1==diff) and (p1!=product):
            marks1=marks1+2
            p2=int(input('Wrong, Enter Product Again:'))
           
            if p2==product:
                 marks1=marks1+1
            else:
                p3=int(input('Again Wrong, Last Chance to Enter Product:'))
                if p3==product:
                    marks1=marks1+1
        elif (s1==sum) and (d1!=diff) and (p1==product):
            marks1=marks1+2
            d2=int(input('Wrong, Enter Difference Again:'))
            if d2==diff:
               marks1=marks1+1
            else:
                d3=int(input('Again Wrong, Last Chance to Enter Product:'))
                if d3==diff:
                   marks1=marks1+1
        elif (s1!=sum) and (d1==diff) and (p1==product):
            marks1=marks1+2
            s2=int(input('Wrong, Enter Sum Again:'))
            if s2==sum:
               marks1=marks1+1
            else:
                 s3=int(input('Again Wrong, Last Chance to Enter Sum:'))
                 if s3==sum:
                     marks1=marks1+1
        
    
    print('OBTAINED MARKS=',marks1)
main()
        