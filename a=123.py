min=int(input('enter number of minutes='))
hours=min//3600
minutes=(min-(hours*3600))//60
print('hour=',hours)
seconds=(min-(hours*3600))%60
print('minutes=',minutes)
print('seconds=',seconds)
print()
print()
a=0o123
b=0x123
c="abs"
print((a))
print((b))
print((c))
print()
print()
a=int(input('enter a='))
b=int(input('enter b='))
x=a**2
y=b**2
z=2*(a*b)
formula=x+y+z
print('result:',formula)