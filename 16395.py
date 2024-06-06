n,k = map(int,input().split())
pas=[[1 for _ in range(j+1)] for j in range(n)]
# print(pas)
for i in range(n):
    for j in range(1,i):
        pas[i][j] = pas[i-1][j] + pas[i-1][j-1]
# print(pas)
print(pas[n-1][k-1])