i=1
while(i!=101):
    temp=i
    rem = 0
    res = 0
    while (temp != 0):
        rem = temp % 10
        res = res * 10 + rem
        temp = temp // 10
    if res == i:
        print(i)
    i+=1
