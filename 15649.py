#15649
def dfs(depth):
  if depth == m:
    print(*out)
    return
  for i in range(n):
    if a[i] not in out:
      out.append(a[i])
      dfs(depth+1)
      out.pop()
n,m = map(int,input().split())
a=[i+1 for i in range(n)]
out = []
dfs(0)
