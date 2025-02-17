import sys
input = sys.stdin.readline

def eratosthenes_sieve(n):
    # n까지의 숫자 리스트 생성
    primes = [True] * (n + 1)#0 ~ n
    p = 2
    while p * p <= n:
        # primes[p]가 아직 True이면 소수임
        if primes[p]:# 소수인가?
            # p의 배수를 모두 False로 설정
            for i in range(p * p, n + 1, p):# 간격이 p, p*p부터 시작됨.
                primes[i] = False
        p += 1
    # 소수 리스트 반환
    return [p for p in range(2, n + 1) if primes[p]]

#input
l = []
while 1:
    a = int(input())
    if a == 0:
        break
    else:
        l.append(a)

#primes list
n=1000000
primes = eratosthenes_sieve(n)
primes_set = set(primes)# 시간초과문제 해결 -> in을 사용할때 set에서 in을 사용하는게 list에서 in을 사용하는거보다 훨씬 빠름
# list에서의 in -> O(n)
# set에서의 in -> O(1)
# 시간차이가 크다


for num in l:# 각 숫자
    res=[]# 만족하는 두 수를 저장하는 리스트
    for num1 in primes:# 하나의 소수 선택(작은 것 부터 탐색)
        num2 = num - num1# num2 -> num1과 짝인 소수
        if num2 < num1:# (num2 > num1) -> 탐색그만 -> 반 지날때까지 못 찾았다.(쌍을 이룰 것이므로) -> 추측 틀림
            print("Goldbach's conjecture is wrong.")
            break# 다음 수에 대해서 탐색
        else:# 아직 반절 안 갔다.(num1 < n/2) == (num1 > num2) (둘 다 같은 소리임)
            if num2 in primes_set:# num2가 소수다 -> 만족(처음 찾은 쌍이 요소간의 차이가 가장 큰 쌍이라고 할 수 있음) -> 원하는 것을 찾음(출력 후 break)
                print(f"{num} = {num1} + {num2}")
                break# 다음 수에 대해서 탐색
