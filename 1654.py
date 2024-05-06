#1654
#이분탐색
import sys
input = sys.stdin.readline 
k,n = map(int, input().split())
l=[int(input()) for _ in range(k)]
start,end = 1,max(l)#최소 최대 값
while start <= end:#start가 end 보다 커질때까지 반복
  mid = (start + end) // 2#중간 값
  line = 0#자른랜선의 개수를 기준으로 탐색할거임
  for i in l:#mid 길이로 잘라서 자른 랜선의 개수를 센다
    line += i//mid
  if line >= n:#더 많은 양의 랜선이 나왔을때
    start = mid+1#자르는 길이를 늘린다.
  elif line < n:#더 적은 양의 랜선이 나왔을때
    end = mid-1#랜선의 길이를 줄인다.
print(end)
