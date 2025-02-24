#11726

# import sys
# input = sys.stdin.readline

# def solve(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return solve(n-1) + solve(n-2)

# if __name__ == "__main__":
#     n = int(input())
#     print(solve(n))
# 시간초과



import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    else:
        DP = [0] * n
        DP[0] = 1
        DP[1] = 2
        for i in range(2,n):
            DP[i] = DP[i-1] + DP[i-2]
        print(DP[n-1]%10007)
