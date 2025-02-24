#1149
import sys
input = sys.stdin.readline

if __name__ == '__main__':
    # input
    n = int(input())
    L = []
    for i in range(n):
        L.append(list(map(int,input().split())))

    # setting
    R = [float('inf')] * n
    G = [float('inf')] * n
    B = [float('inf')] * n
    R[0] = L[0][0]
    G[0] = L[0][1]
    B[0] = L[0][2]

    # main
    for i in range(1,n):
        R[i] = min(G[i-1] + L[i][0], B[i-1] + L[i][0])
        G[i] = min(R[i-1] + L[i][1], B[i-1] + L[i][1])
        B[i] = min(R[i-1] + L[i][2], G[i-1] + L[i][2])

    # output
    print(min(R[-1],G[-1],B[-1]))
