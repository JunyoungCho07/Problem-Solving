import sys
input = sys.stdin.readline

def graph_input(m):
    for i in range(m):
        x,y = map(int,input().split())
        S[x][y] = 1
        S[y][x] = 1

# def solve(n):
#     for i in range(1,n+1):# 모든 컴퓨터에 대해서
#         if virus[i] == 1:# 바이러스걸렸냐?
#             for j in range(1,n+1):
#                 if S[i][j] == 1:# 바이러스 걸린애랑 연결됬냐?
#                     virus[j] = 1# 감염

# def solve2(n):
#     for i in range(1,n+1):# 모든 컴퓨터에 대해서
#         for j in range(1,n+1):
#             if (virus[i] == 1 and S[i][j] == 1) or (virus[j] == 1 and S[i][j] == 1):# 바이러스걸렸냐?
#                 virus[j] = 1

def infect(k: int):
    virus[k] = 1# 감염되었다.
    for i in range(1,n+1):# 모든 컴퓨터에 대해서
        if virus[i] != 1 and S[k][i] == 1:# 감염된 컴터랑 연결되었지만 아직 감염되지 않은 컴퓨터
            infect(i)# 감염시킴

# def print_2d(S):
#     for i in S:
#         for j in i:
#             print(j,end=' ')
#         print()


if __name__ == '__main__':
    #입력
    n = int(input())
    S = [[0 for _ in range(n+1)] for _ in range(n+1)]# 노드는 1부터 세기위해서 0~n+1 생성(인덱스 0번 안씀)
    virus = [0 for _ in range(n+1)]# 바이러스 걸렸냐(인덱스 0번 안씀)
    graph_input(int(input()))
    #S[y][x] == 0 -> 연결 안됨
    #S[y][x] == 1 -> 연결됨
    
    #처리
    infect(1)# 1번 컴퓨터 감염
    
    #출력
    print(virus.count(1)-1)#1번 컴퓨터에 의해 걸리는 컴퓨터의 수 -> 1번컴 제외
    # print_2d(S)

