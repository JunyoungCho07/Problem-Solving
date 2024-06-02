#n,m
#nCm
t= int(input())
for i in range(t):
    n,m = map(int,input().split())
    ans = 1
    for i in range(m-n+1,m+1):
        ans *= i
    for i in range(1,n+1):
        ans //= i
    print(ans)