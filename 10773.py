#10773
t = int(input())
arr = []
for i in range(t):
  a = int(input())
  if a:
    arr.append(a)
  else:
    arr.pop()
print(sum(arr))
