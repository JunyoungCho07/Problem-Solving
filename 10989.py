#10989

#메모리 초과
# import sys
# input = sys.stdin.readline
# t = int(input())
# l = []
# for i in range(t):
#   l.append(int(input()))
# l.sort()
# for i in l:
#   print(i)


#계수정렬 이용
# https://kill-xxx.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-10989%EB%B2%88-%EC%88%98-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-3-%EB%A9%94%EB%AA%A8%EB%A6%AC-%EC%B4%88%EA%B3%BC-%EC%98%A4%EB%A5%98-%ED%95%B4%EA%B2%B0

#계수정렬
import sys
input = sys.stdin.readline
t = int(input())
arr  = [0] * 10001
for i in range(t):
  arr[int(input())] += 1
for i in range(len(arr)):
  if arr[i] != 0:
    for j in range(arr[i]):
      print(i)
