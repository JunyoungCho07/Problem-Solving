#10828
# import sys
# input = sys.stdin.readline

#클래스 사용 연습
"""
class Stack():
  def __init__(self):
    pass
  def push(self, a):
    self.append(a)
  def top(self) -> int:
    if len(self) == 0:
      return -1
    else:
      return self[-1]
  def empty(self) -> int:
    if len(self) == 0:
      return 1
    else:
      return 0
  def pop(self) -> int:
    if len(self) == 0:
      return -1
    return self.pop()
  def size(self) -> int:
    return len(self)

l = []

t=int(input())
for i in range(t):
  st=input()
  if st == "top":
    print(Stack.top(l))
  elif st == "empty":
    print(Stack.empty(l))
  elif st == "size":
    print(Stack.size(l))
  elif st == "pop":
    print(Stack.pop(l))
  else:
    a,b = st.split()
    Stack.push(l,b)
"""

#10828
import sys
input = sys.stdin.readline
t = int(input())
l = []
for _ in range(t):
  operation = list(map(str, input().split()))
  if operation[0] == "push":
    l.append(operation[1])
  elif operation[0] == "top":
    if len(l) == 0:
      print(-1)
    else:
      print(l[-1])
  elif operation[0] == "empty":
    if len(l) == 0:
      print(1)
    else:
      print(0)
  elif operation[0] == "size":
    print(len(l))
  elif operation[0] == "pop":
    if len(l) == 0:
      print(-1)
    else:
      print(l.pop(-1))
    



