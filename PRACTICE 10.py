#TASK1
#(even numbers less than 100 in single line)
def main():

    x=2
    while x<100:
        print (x,end=' ')
        x=x+2
main()
print()
#TASK2
#(input 5 numbers from user and print their sum?)
def main():
    x=int(input('ENTER FIRST DIGIT:'))
    y=int(input('ENTER SECOND DIGIT:'))
    print('Starting Number:',x)
    print('Ending Number:',y)
    while x<y:

        print(x,end=(' '))
        x=x+1
main()    
print()

#TASK3
#(Input 5 numbers from user and print maximum number)
def main():
   i=1
   sum=0
   while i<=5:

      num=int(input('Enter number:'))
      i=i+1
      sum=sum+num
   print('Sum',sum)
main()
print()
#TASK4
#( Input 5 numbers from user and print maximum number?)
def main():
 i=1
 tem=0
 while i<=5:
    x=int(input('Enter value of x='))
    i=i+1
    if x>tem:
      tem=x
     
 print('Highest Number=',tem)
main()

#TASK5
#(Print odd numbers from 49 to 1)
def main():
      x=49
      while x>=1:
        print(x,end=(' '))
        x=x-2
main()