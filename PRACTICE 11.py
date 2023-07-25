#TASK1
from random import*
def main():
     i=1
     while i<=10:
        n1=randint(1,100000)
        n2=randint(1,100000)
        print(f' number 1 is {n1} and number 2 is {n2}')
        if n1>n2:
             print(f' number 1 is larger than number 2 ')
        else:
             print(f' number 2  is larger than number 1')
        i=i+1
        print('-------------------------------------------')
main()     
#TASK2
from random import*
def main():
     i=1
     while i<=10:
          i=i+1
          x1=randint(0,1000)
          x2=randint(0,1000)
          x3=randint(0,1000)
          print( f'Numbers befor sorting are {x1},{x2},{x3}')
          if x1>x2:
             tem=x2
             x2=x1
             x1=tem
          if x2>x3:
             tem=x3
             x3=x2
             x2=tem
          if x3>x2:
             tem=x2
             x2=x3
             x3=tem
          if x1>x2:
             tem=x2
             x2=x1
             x1=tem
          if x2>x3:
             tem=x3
             x3=x2
             x2=tem
          if x1>x2:
             tem=x2
             x2=x1
             x1=tem
          print( f'Numbers after sorting are {x1},{x2},{x3}')
          print('------------------------------------------')
main()
#TASK4
from random import*
def main():
    i=1
    while i<=10:
      i=i+1
      asci=randint(65,90)
      alpha=chr(asci)
      if (asci==65)or(asci==69)or(asci==73)or(asci==79)or(asci==85):
          print(f' Letter is {alpha } and it is Vowel.')
      else:
          print(f' Letter is {alpha } and it is Consonant.')
main()
#TASK5
from random import*
def main():
   i=1
   even=0
   odd=0
   while i<=10:
      i=i+1
      x=randint(0,10)
      print(x,end=(' '))
      if x%2==0:
         even=even+x

      else:
         odd=x+odd
   
   print()
   print('sum of even=',even)
   print('sum of odds=',odd)      
main()

