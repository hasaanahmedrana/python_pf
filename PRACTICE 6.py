basic=int(input('ENTER BASIC SALARY='))
med=0.1*basic
conv=0.15*basic
rent=basic*0.45
gross=basic+med+conv+rent
annualgross=gross*12
tax=0
if annualgross<=200000:
    tax=0
elif annualgross>=200000 and annualgross<=400000:
    tax=0.1*gross
elif annualgross>=400000 and annualgross<=600000:
    tax=0.1*gross
elif annualgross>=600000 and annualgross<=800000:
    tax=0.2*gross
else:
    tax=0.25*gross
net=gross-tax
print('Basic Salary         ',int(basic) )
print('Medical Allowance    ',int (med))
print('Conveyance Allowance',int(conv) )
print('House Rent'           , int (rent))
print('---------------------------')
print('Gross Salary           ',int (gross))
print('Less Tax               ',int (tax))
print('---------------------------')
print('Net Salary           ',int(net))
print()
print()
print()

amount=int(input('AMOUNT DEPOSITED='))
print('Amount Deposited=',amount)
interest1=0.1
interest2=0.07
if amount>500000:
    interest=interest1
else:
    interest=interest2

print(interest)
amount_1=(amount)+(interest*amount)
print('Amount after one year=',int(amount_1))
amount_2=(amount_1)+(interest*amount_1)
print('Amount after two year=',int(amount_2))
amount_3=(amount_2)+(interest*amount_2)
print('Amount after three year=',int(amount_3))

print()
print()
print()
from random import*
x=randint(0,20)
if x==1:
    print(f'Number {x} in English is one')
elif x==2:
    print(f'Number {x} in English is two')
elif x==3:
    print(f'Number {x} in English is three')
elif x==4:
    print(f'Number {x} in English is four')
elif x==5:
    print(f'Number {x} in English is five')
elif x==6:
    print(f'Number {x} in English is six')
elif x==7:
    print(f'Number {x} in English is seven')
elif x==8:
    print(f'Number {x} in English is eight')
elif x==9:
    print(f'Number {x} in English is nine')
elif x==10:
    print(f'Number {x} in English is ten')
elif x==11:
    print(f'Number {x} in English is eleven')
elif x==12:
    print(f'Number {x} in English is twelve')
elif x==13:
    print(f'Number {x} in English is thirteen')
elif x==14:
    print(f'Number {x} in English is fourteen')
elif x==15:
    print(f'Number {x} in English is fifteen')
elif x==16:
    print(f'Number {x} in English is sixteen')
elif x==17:
    print(f'Number {x} in English is seventeen')
elif x==18:
    print(f'Number {x} in English is eighteen')
elif x==19:
    print(f'Number {x} in English is nighteen')
elif x==20:
    print(f'Number {x} in English is twenty')
else:
    print(f'Number {x} in English is zero')

