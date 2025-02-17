def dfs(idx,num,size):
    global cnt
    if idx == n:
        return
    if num + l[idx]== s and size+1 != 0:#10, 100, 1000 이렇게 안하면 똑같은거 계속 세어짐
        cnt += 1
    dfs(idx+1, num + l[idx],size+1)#이 경우를 cnt로 세는거임
    dfs(idx+1,num,size)

cnt = 0
n,s = map(int,input().split())
l = list(map(int,input().split()))
dfs(0,0,0)
print(cnt)