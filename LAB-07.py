#TASK-1
'''from random import*
i=1
marks=1
while i<=10:
    a=randint(1,3)
    if a==1:
        print('Addition:')
        n1=randint(0,99)
        n2=randint(0,99)
        sum=n1+n2
        print('N1:',n1)
        print('N2:',n2)
        result=int(input('Result:'))
        if sum== result:
            print('Correct')
            marks=marks+1
        else:
            print('Incorrect')
        i=i+1
    if a==2:
        print('Subtraction:')
        n1=randint(10,99)
        n2=randint(1,9)
        diff=n1-n2
        print('N1:',n1)
        print('N2:',n2)
        result=int(input('Result:'))
        if diff== result:
            print('Correct')
            marks=marks+1
        else:
            print('Incorrect')
        i=i+1
    if a==3:
        print('Multiplication:')
        n1=randint(0,99)
        n2=randint(0,99)
        product=n1*n2
        print('N1:',n1)
        print('N2:',n2)
        result=int(input('Result:'))
        if product== result:
            print('Correct')
            marks=marks+1
        else:
            print('Incorrect')
        i=i+1
print('SCORE:',marks)
print()
print()
print()    '''
#TASK2
from random import*
i=1
classsum=0
summid=0
sumsess=0
sumfinal=0
fail=0
passstu=0
maxtotal=0
maxmid=0
maxsess=0
maxfinal=0
maxsum=0
minsum=101
minmid=101
minsess=101
minfinal=101
mintotal=0

print(f'Roll No.\t Mid\tFinal\t Session\tTotal\tGrade')
while i <=30:
    mid=randint(1,35)
    final=randint(1,45)
    sess=randint(1,20)
    sum=mid+final+sess
    if sum>maxtotal:
       maxtotal=sum
    if mid>maxmid:
       maxmid=mid
    if final>maxfinal:
        maxfinal=final
    if sess>maxsess:
        maxsess=sess
    if sum>maxsum:
        maxsum=sum
    if sum<minsum:
        minsum=sum
    if mid<minmid:
        minmid=mid
    if sess<minsess:
        minsess=sess
    if final<minfinal:
        minfinal=final
    if sum>=50:
        passstu=passstu+1
    if sum<50:
        fail=fail+1

    
    if (sum>95):
        grade='A+'
    elif (sum>90):
        grade='A'
    elif (sum>85):
        grade='B+'
    elif (sum>80):
        grade='B-'
    elif(sum>75):
        grade='C+'
    elif(sum>70):
        grade='C'
    elif(sum>65):
        grade='C-'
    elif(sum>60):
        grade='D+'
    elif (sum>55):
        grade='D-'
    elif (sum<50):
        grade='F'
       
    
    
    print(f'{i}\t\t {mid}\t{final}\t {sess}\t\t{sum}\t {grade}')
    
    i=i+1
    classsum=classsum+sum
    ave=classsum/30
    summid=summid+mid
    midave=summid/(30)
    sumsess=sumsess+sess
    sessave=sumsess/30
    sumfinal=sumfinal+final
    finalave=sumfinal/30
print('Pass',passstu)
print('Fail',fail)
print('Overall Class Average:',ave)
print('Average Mid Term marks:',midave)
print('Average Sessional  marks:',sessave)
print('Average Final Term marks:',finalave)
print('Maximum  Marks:',maxsum)
print('Maximum Total Marks:',maxtotal)
print('Maximum Mid Marks:',maxmid)
print('Maximum Sessional Marks:',maxsess)
print('Maximum Final Term Marks:',maxfinal)
print('Minimum Marks:',minsum)
print('Minimum Mid Term Marks:',minmid)
print('Minimum Sessional Marks:',minsess)
print('Minimum Final Term Marks:',minfinal)