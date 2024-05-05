#10866
import sys
input = sys.stdin.readline
t = int(input())
l = []
for _ in range(t):
  operation = list(map(str, input().split()))
  if operation[0] == "push_back":
    l.append(operation[1])
  if operation[0] == "push_front":
    l.insert(0, operation[1])
  elif operation[0] == "back":
    if len(l) == 0:
      print(-1)
    else:
      print(l[-1])
  elif operation[0] == "front":
    if len(l) == 0:
      print(-1)
    else:
      print(l[0])
  elif operation[0] == "empty":
    if len(l) == 0:
      print(1)
    else:
      print(0)
  elif operation[0] == "size":
    print(len(l))
  elif operation[0] == "pop_back":
    if len(l) == 0:
      print(-1)
    else:
      print(l.pop(-1))
  elif operation[0] == "pop_front":
    if len(l) == 0:
      print(-1)
    else:
      print(l.pop(0))
  # print("{}".format(_), l)
