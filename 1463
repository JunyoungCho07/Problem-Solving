#1463
n = int(input())
dp = [i for i in range(n+1)]
dp[1] = 0
for i in range(1,n+1):
  if i == 1 or dp[i] != 0:
    if 2*i <= n:
      dp[2*i] = min(dp[2*i],dp[i]+1)
    if 3*i <= n:
      dp[3*i] = min(dp[3*i],dp[i]+1)
    if i+1 <= n:
      dp[i+1] = min(dp[i+1],dp[i]+1)
    if i+2 <= n:
      dp[i+2] = min(dp[i+2],dp[i]+2)
print(dp[n])
