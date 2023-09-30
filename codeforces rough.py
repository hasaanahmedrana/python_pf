#PROBLEM-A
from itertools import permutations
n=int(input('N:'))
for i in range (n):

    a=list(permutations(input('')))
    b=set(a)
    c=list(b)
    count=0
    for i in range (len(c)):
        a=list(c[i])
        d=list(c[i])
        d.reverse()    
        if a==d:
            count+=1
    print(count)

#PROBLEM-B
def result(l):
    p,n=map(int,input().split())
    s=list(map(int,input().split()))
    team1=[]
    team2=[]
    for i in range (p):
        team1.append((s[i]))
    for i in range (p,2*p):
        team2.append(s[i])
    print(team1)
    print(team2)
    for i in range (p-1):
        diff=abs(int(team1[i])-int(team2[i]))
        if team1[i]>team2[i]:
            team1[i+1]+=diff
        else:
            team2[i+1]+=diff

    last=abs(team1[p-1]-team2[p-1])
    print(f'Case#{l+1}:',end=' ')
    if last==n:
        print('Tie')
    else:
        print('Destruction')

def main():
    num=int(input()) 
    for l in range (num):
        result(l)
main()

#PROBMLEM-C
n=int(input('N:'))
for i in range (n):
    r=int(input(''))
    sum=0
    for j in range (1,r):
        if j%3==0 or j%5==0:
            sum+=j
    print(sum)


PROBLEM-D
n=int(input('N:'))
for i in range (n):
    l=[' ','',64,67,70,73,76,79,83,86]
    s=input('')
    i=0
    while i < len(s):
        a=s[i]
        count=0
        for j in range (i,len(s)):
            if s[j]==a:
                count+=1
            else:
                break
        if a=="#":
            i+=1
        elif a=="0":
            print(end=' ')
            i+=count
        else:
            print(chr(l[int(a)]+count),end='')
            i+=count



#PROBLEM-E
n=int(input('N:'))
for i in range (n):
    inp=list(input(''))
    vowels=['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for j in range (len(inp)):
        if inp[j] in vowels:
            for k in range (j,len(inp)):
                if inp[k] in vowels:
                    inp[k],inp[j]=inp[j],inp[k]
    sti="".join(inp)
    print(sti)


#cipher
n=int(input(''))
l=list(input())
k=int(input(''))
for i in range (len(l)):
    a=ord(l[i])
    if a>64 and a<91 and a+k<91:
        l[i]=chr(a+k)
    elif a>96 and a<123 and a+k<123:
        l[i]=chr(a+k)
    elif a>64 and a<91 and a+k>90:
        l[i]=chr(64+(a+k-90))
    elif a>96 and a<123 and a+k>122:
        l[i]=chr(96+(a+k-122))
s=''.join(l)
print(s)


n = int(input())
s = input()
k = int(input())
encrypted_string = ""
for i in range(len(s)):
    a = ord(s[i])
    if 65 <= a <= 90:  # Uppercase letters
        encrypted_char = chr((a - 65 + k) % 26 + 65)
    elif 97 <= a <= 122:  # Lowercase letters
        encrypted_char = chr((a - 97 + k) % 26 + 97)
    else:  # Non-alphabetic characters
        encrypted_char = s[i]
    encrypted_string += encrypted_char
print(encrypted_string)
 
n=int(input(''))
for i in range (n):
    marks=int(input(''))
    if marks%5!=0:
        b=0
        for j in range (1,5):
            if (marks+j)%5==0:
                b=marks+j
                break
        if b>=40 and b!=0 and b-marks<3:
            marks=b
    print(marks)


set1={2,6,8,4}
set2={0,1,2,3,4,5,6,7,8,8,8,}
print(set1)
print(set2)
print(set2<=(set1))

def main():
    s=input('')
    k=int(input())
    new_s=''
    for char in s:
        a=ord(char)
        if 65 <= a <= 90:
            new_char=chr ((a+k-65) % 26 + 65)
        elif 97 <= a <= 122:
            new_char=chr ((a+k-97) %26 + 97)
        else:
            new_char=char
        new_s+=new_char
    print(new_s)
main()

 bigsorting   
def main():
    n=int(input())
    list=[]
    for i in range (n):
        num=(input())
        list.append(num)
    list.sort(key=lambda x: (len(x), int(x)))
    for number in list:
        print(number)
main()

def further(a):
    for i in range(len(a)):
        n=a[i]
        a.pop(i)
        b=a.copy()
        b.reverse()
        if a==b:
            return i
        else:
            a.insert(i,n)
    return 0
def check(word):
    a=list(word)
    b=list(word)
    b.reverse()
    if a==b:
        print(-1)
    else:
        print(further(a))

def main():
    n=int(input())
    for i in range (n):
        word=(input())
        (check(word))
main()



integer=list(map(int,input().split()))
points=[1]*len(integer)
for i in range(1,len(integer)):
    if integer[i]<=integer[i-1]:
        points[i]=points[i-1]-1
        if points[i]==0:
            points[i]=1
            for j in range (i):
                points[j]+=1
    elif integer[i]>integer[i-1]:
        points[i]=points[i-1]+1
print(sum(points))



def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 1
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)





def alreadyokay():
    s=list(input())
    if s==s[::-1]:
       return -1
    else:
       return ispalindrome(s)
def ispalindrome(s):
    ans=-1
    for i in range (len(s)-1,-1,-1):
        a=s[i]
        s.pop(i)
        if s==s[::-1]:
            ans=i
            return ans
            break
        else:
            s.insert(i,a)
    return ans


def main():
    t=int(input())
    for i in range(t):
        print(alreadyokay())
main()
      


n = int(input())
count = 0
socks = list(map(int,input().split()))
i = 0
while i < len(socks):
    j = i + 1
    while j < len(socks):
        if socks[j] == socks[i]:
            count += 1
            socks.pop(j)
            socks.pop(i)
            i -= 1  # Adjust index after removing the first item
            break
        j += 1
    i += 1
print(count)


n=int(input())
page=int(input())
if n%2==0:
    pages1=0
    count=0
    for j in range (1,page):
        count+=1
    pages1=count//2+count%2
    pages2=0
    count=0
    for k in range(n-1,page-1,-1):
        count+=1
    pages2=count//2+count%2
else:
    pages1=0
    count=0
    for j in range (1,page):
        count+=1
    pages1=count//2+count%2
    pages2=0
    count=0
    for k in range(n-2,page-1,-1):
        count+=1
    pages2=count//2+count%2

if pages1<pages2:
    print(pages1)
else:
    print(pages2)





def cat():
    cat_a,cat_b,mouse=map(int,input().split())
    dist1=abs(cat_a-mouse)
    dist2=abs(cat_b-mouse)
    if dist1<dist2:
        print("Cat A")
    elif dist1>dist2:
        print('Cat B')
    else:
        print("Mouse C")

def main():
    n=int(input())
    for i in range(n):
        cat()
main()



