import sys
input = sys.stdin.readline

# def f(m,cnt):# m원 만들어야함, 동전 cnt개 씀
#     global ans
#     if cnt >= ans:
#         return
#     if m == 0:
#         ans = min(ans,cnt)
#         return
#     else:
#         for i in range(len(coin_type)):
#             if coin_type[i] <= m:
#                 f(m-coin_type[i],cnt+1)
def greed(m):
    cnt = 0
    for i in range(len(coin_type)):
        if m >= coin_type[i]:
            cnt += m//coin_type[i]
            m = m%coin_type[i]
    return cnt
n,m = map(int,input().split())
coin_type = []
for i in range(n):
    coin_type.append(int(input()))
coin_type.sort(reverse=True)
ans = greed(m)
# f(m,0)
# (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수) 배수라는 조건 때문에 그리디 알고리즘이 최적해를 보장한가도 할 수 있음음
print(ans)
#시간이 너무 오래 걸림

