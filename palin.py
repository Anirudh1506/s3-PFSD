def palin(n):
    temp=n
    rem=0
    res=0
    while(temp!=0):
        rem=temp%10
        res=res*10+rem
        temp=temp//10
    if res==n:
        print("YES")
    else:
        print("NO")
a=int(input())
palin(a)