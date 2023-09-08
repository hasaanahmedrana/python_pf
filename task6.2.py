num3=randint(1,5)
num4=randint(1,5)
print(num3)
print(num4)
if num3==num4:
    print('numbers are exactly equal')
if (abs(num3-num4))>=2 and (abs(num4-num3)>=2):
    print('not equal')
if (abs(num3-num4))==1 and (abs(num4-num3))==1:
    print('almost equal')