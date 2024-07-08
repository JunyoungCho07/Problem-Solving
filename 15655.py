#15655
def dfs(depth,idx):
  if depth == m:
    print(*out)
    return
  for i in range(idx,n):
    out.append(a[i])
    dfs(depth+1,i+1)
    out.pop()
n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
out = []
dfs(0,0)
