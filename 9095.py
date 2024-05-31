#9095
import sys
input = sys.stdin.readline
def f(n):
  if n == 0:
    return 1
  elif n < 0:
    return 0
  else:
    return sum(f(n-i) for i in range(1,4))
if __name__ == '__main__':
  t = int(input())
  for _ in range(t):
    n = int(input())
    print(f(n))
