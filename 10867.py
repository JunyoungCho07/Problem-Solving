n = int(input())
l = list(map(int,input().split()))
ans = sorted(set(l))
print(*ans)
