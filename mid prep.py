s1=int(input('USER 1 DECIDE 0 OR 1 AS HIS/HER SYMBOL:'))
if s1=='O' :
    replace1=0
s2=int(input('USER 2 DECIDE 0 OR 1 AS HIS/HER SYMBOL:'))
if s2=='O' :
    replace2=0
else:
     replace2=1
i=0
a1='a1'
a2='a2'
a3='a3'
b1='b1'
b2='b2'
b3='b3'
c1='c1'
c2='c2'
c3='c3'
l1=(f'{a1} | {a2} | {a3}')
l2=(f'-------------')
l3=(f'{b1} | {b2} | {b3}')
l4=(f'-------------')
l5=(f'{c1} | {c2} | {c3}')
print(f'{l1}\n{l2}\n{l3}\n{l4}\n{l5}') 
i=1
while  (a1==a2 and a2==a3) or  (b1==b2 and b2==b3) or  (c1==c2  and c2==c3) or  (a1==b2 and  b2==b3) or (a3==b2 and b2==c1):
   user1=input('Enter position name:')
   if i%2!=0:
      user1=input('Enter position name:')
      user1=replace1
   if i%2==0:
       user2=input('Enter position name:')
       user2=replace2
print(f'{l1}\n{l2}\n{l3}\n{l4}\n{l5}')
i=i+1



