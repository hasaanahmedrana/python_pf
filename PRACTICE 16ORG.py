#TASK5
'''def main():
    x=int(input('Enter Number :'))
    i=2
    while i <=x:
        if x%i==0:
            print(f' {x} is divisible by {i}')
        i=i+1    

main()'''
def main():
    a=int(input('Enter Number 1:'))
    b=int(input('Enter Number 2:'))
    c=int(input('Enter Number 3:'))
    d=int(input('Enter Number 4:'))
    e=int(input('Enter Number 5:'))
    print(f'ELEMENT 1:{a}\nELEMENT 2:{b}\nELEMENT 3:{c}\nElement 4:{d}\nELEMENT 5:{e}')
    print('Difference of element 1: ' ,end=' ')
    difference=a-b
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=a-c
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=a-d
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=a-e
    if difference<0:
        difference=-(difference)
    print(difference)
    print('Difference of element 2: ' ,end=' ')
    difference=b-a
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=b-c
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=b-d
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=b-e
    if difference<0:
        difference=-(difference)
    print(difference)
        
    print('Difference of element 3: ' ,end=' ')
    difference=c-a
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=c-b
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=c-d
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=c-e
    if difference<0:
        difference=-(difference)
    print(difference)
        
    print('Difference of element 4: ' ,end=' ')
    difference=d-a
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=d-b
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=d-c
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=d-e
    if difference<0:
        difference=-(difference)
    print(difference)
        
    print('Difference of element 5: ' ,end=' ')
    difference=a-d
    if difference<0:
        difference=-(difference)
        print(difference,end=' ');
    difference=d-b
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=c-d
    if difference<0:
        difference=-(difference)
    print(difference,end=' ');
    difference=d-e
    if difference<0:
        difference=-(difference)
    print(difference)
        


main()
