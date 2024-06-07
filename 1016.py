#시간초과
'''
def fil1(arr, k):#filter 
    for j in range(2,k+1):
        for i in range(len(arr)):
            if arr[i] % j**(2) == 0:
                arr[i]=0 #제곱 ㄴㄴ 수 아닌 값 0으로 바꿈
    return arr

if __name__ == '__main__':
    min, max = map(int,input().split())
    #2**(2) ~ int(max**(0.5))**(2)
    arr = [i for i in range(min,max+1)]
    k = int(max**(0.5))
    arr = fil(arr,k)
    arr = [x for x in arr if x != 0]#0 제거
    print(len(arr))#valid한 값의 개수 count
'''



#최종 코드
import sys
input = sys.stdin.readline
def fil2(min,max):#아래에 있는 에라토스테네스 체 코드 모방
    #is_nosqrt의 범위 줄이는 부분은 GPT도움을 받음
    range_size = max - min + 1
    is_nosqrt = [True] * range_size
    for i in range(2,int(max**(0.5))+1):
        square = i * i
        start = ((min + square - 1) // square) * square
        #is_nosqrt[0] -> min, is_nosqrt[1] -> min+1 
        # start = ((min + square - 1) // square) * square #by GPT
        # (min + square - 1) // square는 min / square가 나누어 떨어지지 않을때
        # min / square를 올림하는 역할을 함
        #start = int((min/square)+1) 로 쓰면 안됨 -> 경계값 문제 발생 ex)min = 16, square = 4  
        for j in range(start, max + 1, square):
            is_nosqrt[j - min] = False
    return sum(is_nosqrt)

if __name__ == '__main__':
    min, max = map(int,input().split())
    #2**(2) ~ int(max**(0.5))**(2)
    print(fil2(min,max))


#에라토스테네스의 체 by copilot
'''
import math

def sieve_of_eratosthenes(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    is_prime = [True] * (n + 1)  # 처음엔 모든 수가 소수(True)인 것으로 초기화 (0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:  # i가 소수인 경우 (남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            for j in range(2 * i, n + 1, i):
                is_prime[j] = False

    # 소수만 반환
    primes = [i for i in range(2, n + 1) if is_prime[i]]
    return primes
'''
