def Ifreached(time):
    if(time>=30):
        return 'YES'
    else:
        return 'NO'
n=int(input())
for i in range(n):
    print(Ifreached(int(input())))
