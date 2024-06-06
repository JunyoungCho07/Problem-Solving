n = int(input())
l = list(map(int,input().split()))
s = []
#증가하는지 감소하는지에 대한 정보를 담은 리스트 생성
for i in range(n-1):
    if l[i+1]-l[i] > 0:
        a = 1
    elif l[i+1]-l[i] == 0:
        a = 0
    else:
        a = -1
    s.append(a)
# print(s)

#연속으로 증가 or 감소하는지 count하는 함수 필요
cnt_1 = 0
cnt_2 = 0
res = []
for i in range(len(s)):
    #증가
    if s[i] == 1 or s[i] == 0:
        cnt_1 += 1
    elif s[i] == -1:
        res.append(cnt_1+1)
        cnt_1 = 0
    #감소
    if s[i] == -1 or s[i] == 0:
        cnt_2 += 1
    elif s[i] == 1:
        res.append(cnt_2+1)
        cnt_2 = 0

#마지막 카운트 하던 값도 추가해줌(처음 풀었을때 틀린 부분)
res.append(cnt_1+1)
res.append(cnt_2+1)

#가장 긴 수열 출력
print(max(res))
