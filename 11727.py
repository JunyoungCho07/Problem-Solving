#11727
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(3)
    else:
        DP = [0] * n
        DP[0] = 1
        DP[1] = 3
        for i in range(2,n):
            DP[i] = DP[i-1] + 2*DP[i-2]
        print(DP[-1]%10007)