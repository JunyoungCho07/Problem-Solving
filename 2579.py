#2579
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    w = []
    for i in range(n):
        w.append(int(input()))

    if n == 1:
        print(w[0])
    elif n == 2:
        print(max(w[1], w[0] + w[1]))
    else:
        DP = [0] * n
        DP[0] = w[0]
        DP[1] = max(w[1],w[0] + w[1])
        for i in range(2, n):
            if i == 2:
                DP[i] = max(w[i] + w[i-1], w[i] + w[i-2])
            else:
                DP[i] = max(DP[i-2] + w[i], DP[i-3] + w[i-1] + w[i])
        print(DP[n-1])