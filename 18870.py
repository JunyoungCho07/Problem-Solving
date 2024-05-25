#18870
import sys
input = sys.stdin.readline

#입력
n = int(input())
arr = list(map(int,input().split()))

#데이터 가공
tmp = arr[:]
tmp = list(set(tmp))#중복값 제거
tmp.sort()#정렬 -> 인덱스 = 압축된 좌표

#IDEA
dict = {}
for index, num in enumerate(tmp):#인덱스 = 압축된 좌표 이므로 enumerate 사용
    dict[num] = index#key = 숫자, value = 압축된 좌표

#출력
for i in range(n):
    print(dict[arr[i]], end=' ')
