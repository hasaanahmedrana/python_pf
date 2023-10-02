def check2(a,b,length):
    for j in range (length):
        if a[j]<b[j]:
            return False
    return True
def check():
    length=int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if a==b:
        return "Yes"
    for i in range(length):
        if a[i] < b[i]:
            return "NO"
    if max(a)<max(b):
        return 'NO'
    maxi=max(a)
    for i in range (maxi):
        a=[j-1 if j!=0 else j for j in a]
        if not check2(a,b,length) :
            return "NO"
        if a==b:
            return "Yes"
    return "NO"

def main():
    t=int(input())
    for i in range (t):
        print(check())
main()