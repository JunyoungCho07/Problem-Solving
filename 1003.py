#1003
#DP
zeros = [1 , 0]#0 호출횟수
ones=[0 , 1]#1 호출횟수
for i in range(2,41):
    zeros.append(zeros[i-2]+zeros[i-1])
    ones.append(ones[i-2]+ones[i-1])

t = int(input())
for i in range(t):
    a = int(input())
    print(zeros[a], ones[a])