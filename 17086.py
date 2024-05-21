# directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]
# def solve():
#     for i in range(n):
#         for k in range(m):
#             if not l[i][k]:
#                 l[i][k]=f(i,k,1)

# def f(i,k,cnt) -> int:#cnt는 search범위 나타냄
#     for x,y in directions:
#         try:
#             if l[i+x*cnt][k+y*cnt]==-1:
#                 return cnt
#         except: pass
#     return f(i,k,cnt+1)
    
# # def safe(x,y) -> bool:
# #     if 0 <= x < n and 0 <= y < m:
# #         return True
# #     else: return False


# if __name__ == "__main__":
#     n, m = map(int,input().split())
#     l=[]
#     for i in range(n):
#         l.append(list(map(int,input().split())))

#     # for i in range(n):
#     #     for k in range(m):
#     #         if l[i][k] == 1:
#     #             l[i][k] = -1
#     l = [[-1 if x == 1 else x for x in row] for row in l]

#     solve()
#     #max(1차원 배열로 변환)
#     flat_data = [item for sublist in l for item in sublist]
#     print(max(flat_data))



#float('inf')는 IEEE 754 부동소수점 표준 무한대를 나타냄
# print(float('inf'))
# print(type(float('inf')))



from collections import deque
directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)]

def solve(n,m,grid):
    #BFS 초기설정
    queue = deque()
    distance = [[float('inf')]*m for _ in range(n)]

    #아기 상어가 있는 위치를 큐에 추가하고, 초기 거리를 0으로 설정
    for i in range(n):
        for k in range(m):
            if grid[i][k] ==1:
                queue.append((i,k))
                distance[i][k] = 0
    while queue:
        x,y = queue.popleft()
        for dx,dy in directions:
            nx,ny = x+dx,y+dy #new x, new y
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == float('inf'):
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx,ny))
    max_distance = 0
    for i in range(n):
        for k in range(m):
            if distance[i][k] != float('inf'):
                max_distance = max(max_distance, distance[i][k])
    return max_distance

if __name__ == "__main__":
    n,m = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int,input().split())))
    
    result = solve(n,m,grid)
    print(result)