#1920
n = int(input())
val = set(map(int, input().split()))
m = int(input())
chk = list(map(int, input().split()))
for el in chk:
  if el in val:
    print(1)
  else:
    print(0)
