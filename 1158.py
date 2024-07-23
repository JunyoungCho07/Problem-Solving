n, k = map(int, input().split())
l = [i+1 for i in range(n)]
res = []
s = 0
while l :
    s += (k-1)
    while s > len(l)-1:
        s -= len(l)
    res.append(l.pop(s))
print('<',end='')
print(*res, sep=', ',end='')
print('>',end='')