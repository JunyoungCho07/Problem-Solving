#11866
n,k = map(int,input().split())
l = [i for i in range(1,n+1)]
result = []
p=0
for i in range(n):
  p=p+k-1#k씩 건너뛰며 제거 값 제거하면 1개씩 밀리므로 -1이 있는것임
  while p >= len(l):#인덱스 밖일때 값 조정
    p = p-len(l)
  result.append(l.pop(p))#요세푸스 순열을 순서대로 제거 및 append

#output
for i in range(n):
  if i == 0:
    print("<",end="")
  if i != n-1:
    print(result[i], end=", ")
  elif i == n-1:
    print(result[i],end = "")
    print(">")
  
