#10816
#Hashing 해쉬 알고리즘 방식
#딕셔너리로 구현함
import sys
input = sys.stdin.readline
_ = int(input())
val = sorted(map(int, input().split()))
_ = int(input())
chk = list(map(int, input().split()))
hashmap={}
for i in val:
  if i in hashmap:# i 가 hashmap의 key 역할을 함
    hashmap[i] += 1#vlaue는 개수 역할, 개수 1 증가
  else:
    hashmap[i] = 1#없었다면 1개 찾은것 이므로 valuefmf 1 로 딕셔너리에 추가

#output
for i in chk:
  if i in hashmap:
    print(hashmap[i], end=' ')
  else:
    print('0' , end=' ')


#https://chancoding.tistory.com/45
