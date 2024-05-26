n = int(input())
nl = list(map(int,input().split()))
m = int(input())
ml = list(map(int,input().split()))
nl = set(nl)
for i in ml:
    if i in nl:
        print(1,end = ' ')
    else:
        print(0,end=' ')