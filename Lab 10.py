# #TASK-1
from random import*
def main():
    list=[8]*12
    print('Monthly Sales:',end=' ')
    for i in range(12):
        list[i]=randint(10,99)
        print(list[i],end='  ')
        # list[i]=int(input(''))
    print()
    print()
    sum_quater_1=0
    print('Quater 1:',end=' ')
    for i in range (3):
        print(list[i],end=' ')
        if i==0:  max1=list[i];  min1=list[i];
        else:
            if max1<list[i]:   max1=list[i] ;
            if min1>list[i]:  min1=list[i];
        sum_quater_1+=list[i]
    average1=sum_quater_1/3
    print(f'\tMIN:{min1}  \t  MAX:{max1} \tAVERAGE:{average1:<2.2f} ')
    sum_quater_2=0
    print('Quater 2:',end=' ')
    for i in range (3,6):
        print(list[i],end=' ')
        if i==3: max2=list[i]; min2=list[i];
        else:
            if max2<list[i]: max2=list[i];
            if min2>list[i]:min2=list[i];
        sum_quater_2+=list[i]
    average2=sum_quater_2/3
    print(f'\tMIN:{min2}  \t  MAX:{max2} \tAVERAGE:{average2:<2.2f} ')
    sum_quater_3=0
    print('Quater 3:',end=' ')
    for i in range (6,9):
        print(list[i],end=' ')
        if i==6:
            max3=list[6]
            min3=list[6]
        else:
            if max3<list[i]: max3=list[i] ;
            if min3>list[i]: min3=list[i] ;
        sum_quater_3+=list[i]
    average3=sum_quater_3/3
    print(f'\tMIN:{min3}  \t  MIN:{max3} \tAVERAGE:{average3:<2.2f} ')
    sum_quater_4=0
    print('Quater 4:',end=' ')
    for i in range (9,12):
        print(list[i],end=' ')
        if i==9:  max4=list[9];  min4=list[9];
        else:
            if max4<list[i]:  max4=list[i];
            if min4>list[i]:  min4=list[i];
        sum_quater_4+=list[i]
    average4=sum_quater_4/3
    print(f'\tMIN:{min4}  \t  MAX:{max4} \tAVERAGE:{average4:<2.2f} ')
    print()
#checking one with minimum sale:
    min_value = min(min1, min2, min3, min4)
    if min_value == min1:
        print(f'Quarter 1 has the minimum sale {min_value}')
    elif min_value == min2:
        print(f'Quarter 2 has the minimum sale {min_value}')
    elif min_value == min3:
        print(f'Quarter 3 has the minimum sale {min_value}')
    else:
        print(f'Quarter 4 has the minimum sale {min_value}')
 #checking one with maximum sale:
    max_value = max(max1, max2, max3, max4)
    if max_value == max1:
        print(f'Quarter 1 has the maximum sale {max_value}')
    elif max_value == max2:
        print(f'Quarter 2 has the maximum sale {max_value}')
    elif max_value == max3:
        print(f'Quarter 3 has the maximum sale {max_value}')
    else:
        print(f'Quarter 4 has the maximum sale {max_value}')
#one with minimum average 
    min_average=min(average4,average2,average3,average1)
    if min_average==average1:
        print(f'Quarter 1 has the minimum average {min_average:<2.2f}')
    elif min_average==average2:
        print(f'Quarter 2 has the minimum average {min_average:<2.2f}')
    elif min_average==average3:
        print(f'Quarter 1 has the minimum average {min_average:<2.2f}')
    else:
        print(f'Quarter 4 has the minimum average  {min_average:<2.2f}')
#one with maximum average 
    max_average=max(average1,average2,average3,average4)
    if max_average==average1:
        print(f'Quarter 1 has the maximum average {max_average:<2.2f}')
    elif max_average==average2:
        print(f'Quarter 2 has the maximum average {max_average:<2.2f}')
    elif max_average==average3:
        print(f'Quarter 1 has the maximum average {max_average:<2.2f}')
    else:
        print(f'Quarter 4 has the maximum average {max_average:<2.2f}')
main()

#TASK-2
from random import*
def main():
    x=[0]*10
    y=[0]*10
    z=[0]*10
    score=0
    for i in range (10):
        x[i]=randint(1,9)
        y[i]=randint(1,9)
        print(f'{x[i]}+{y[i]}=',end=' ')
        z[i]=int(input(''))
        if z[i]==(x[i]+y[i]): 
            score+=1
    print(f'{score}/10')
    print(f'Correct\tIncorrect')
    for i in range(10):
        if z[i]!=(x[i]+y[i]):
            print(f'{x[i]}+{y[i]}={x[i]+y[i]}\t{x[i]}+{y[i]}={z[i]}')
main()



