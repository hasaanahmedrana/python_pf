#TASK1
mask1=2**0
mask2=2**1
mask3=2**2
mask4=2**3
mask5=2**4
mask6=2**5
mask7=2**6
mask8=2**7
x=ord(input('enter alphabet='))
if x&mask1==mask1:
    print('bit 1 is on')
if x&mask2==mask2:
    print('bit 2 is on')
if x&mask3==mask3:
    print('bit 3 is on')
if x&mask4==mask4:
    print('bit 4 is on')
if x&mask5==mask5:
    print('bit 5 is on')
if x&mask6==mask6:
    print('bit 6 is on')
if x&mask7==mask7:
    print('bit 7 is on')
if x&mask8==mask8:
    print('bit 8 is on')



#TASK2
mask1=2**0
mask2=2**1
mask3=2**2
mask4=2**3
mask5=2**4
mask6=2**5
mask7=2**6
mask8=2**7
character1=input('enter characrer 1:')
character2=input('enter characrer 2:')
x=ord(character1)
y=ord(character2)
count=0
if (x&mask1) == (y&mask1) :
   count=count+1
if (x&mask2) == (y&mask2)   :
   count=count+1
if (x&mask3) == (y&mask3):
   count=count+1
if(x&mask4) == (y&mask4) :
   count=count+1
if (x&mask5) == (y&mask5):
   count=count+1
if (x&mask6)==(y&mask6) :
   count=count+1
if (x&mask7)== (y&mask7)  :
   count=count+1
if (x&mask8)== (y&mask8) :
   count=count+1
print('FIRST CHARACTER:',character1)
print('SECOND CHARACTER:',character2)
print(f'In {chr(x)} and {chr(y)}, {count} bits are same')
()
()
#TASK3
#TASK3
#TASK3
c1=input('Enter first characxter=')
c2=input('Enter second characxter=')
bit1=ord(c1)
bit2=ord(c2)
if bit1-bit2==0:
    print(f'{c1} and {c2} are same=')
else:
     print(f'{c1} and {c2} are different=')
#TASK4
#TASK4
#TASK4
character=input('Enter character=')
asci=ord(character)
bitno=int(input('Enter bit position='))
mask=2**(bitno-1)
if asci&mask==mask:
    print(f'The bit number{bitno} is ON in {character}')
else:
        print(f'The bit number{bitno} is OFF in {character}')