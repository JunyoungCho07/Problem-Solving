#1966
t = int(input())
for i in range(t):
  n,m = map(int, input().split())
  a = list(map(int, input().split()))
  p=m #p가 원하는 값의 인덱스
  cnt = 0 #몇번째인지
  while 1:
    if max(a) == a[0] and p != 0:
      a.pop(0)
      cnt += 1
      p -= 1
    elif max(a) == a[0] and p == 0:
      a.pop(0)
      cnt += 1
      print(cnt)
      break
    elif max(a) != a[0] and p == 0:
      a.append(a.pop(0))
      p = len(a)-1
    else:
      a.append(a.pop(0))
      p -= 1
