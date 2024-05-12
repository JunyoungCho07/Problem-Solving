 #1789

s = int(input())
tot = 0
cnt = 0
while 1:
    cnt += 1
    tot += cnt
    if tot > s:
        print(cnt-1)#s를 넘었다면 그 전 값이 유효한 값이기 때문
        break
#하나씩 더하다가 그 값이 s를 넘겼을때 cnt-1을 출력
#1+2+3+4+5+~~
#이 수열의 합의 공식은 아래와 같다.
#sum = (cnt * (cnt+1)) / 2
