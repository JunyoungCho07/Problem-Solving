t = int(input())
reward= []
for i in range(t):
    l = list(map(int,input().split()))
    l.sort()
    a,b,c = l[:]
    if a==b==c:
        reward.append(10000+a*1000)
    elif a==b or b == c:
        reward.append(1000 + b*100)
    else:
        reward.append(100*c)
print(max(reward))
