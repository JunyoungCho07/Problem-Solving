#2108
import sys
input = sys.stdin.readline
t = int(input())
arr = []
for i in range(t):
    arr.append(int(input()))
arr.sort()

#산술평균
avg = round(sum(arr)/len(arr))
print(avg)

#중앙값
print(arr[(len(arr)-1)//2])

#최빈값
# def solution(array):
    # while len(array) != 0:
        # for i, a in enumerate(set(array)):
            # array.remove(a)
        # if i == 0: return a
    # return -1
# print(solution(arr))

dic = {}#num:count
#개수세기
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
# print(dic)
max = max(dic.values())
max_dic=[]
#max 값 모으기
for i in dic:#i=key
    if max == dic[i]:
        max_dic.append(i)
#정렬
max_dic.sort()
#최빈값이 여러개인 경우
if len(max_dic) > 1:
    print(max_dic[1])
#최빈값이 1개인 경우
else:
    print(max_dic[0])

#범위
print(arr[-1] - arr[0])