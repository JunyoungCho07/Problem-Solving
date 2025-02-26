import sys
input = sys.stdin.readline

n = int(input())
l=[]

for i in range(n):
    l.append(int(input()))
l.sort()
l.reverse()

max_weight = float('-inf')
for i in range(n):
    max_weight = max(max_weight, l[i] * (i+1))# l[i]까지의 로프를 사용하면 그 로프가 들 수 있는 최대무게 * 로프의 수(i*1)만큼 들 수 있음.
print(max_weight)