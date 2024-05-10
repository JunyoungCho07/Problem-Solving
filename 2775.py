#2775
import sys
input = sys.stdin.readline
#재귀
# def f(h,x):
#   if h == 0:
#     return x
#   else:
#     return sum(f(h-1,x-i) for i in range(0,x))

#DP
arr = [[i for i in range(15)]]
for i in range(15):#0~14
  tmp=[]
  for k in range(15):
    tmp.append(sum(arr[i][0:k+1]))#전 층 i에 대해서 0~k호까지의 인원수 합
  arr.append(tmp)

#Main
t = int(input())
for i in range(t):
  k = int(input())
  n = int(input())
  print(arr[k][n])
