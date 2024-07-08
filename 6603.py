#내가 짰는데 너무 임시방편들이 많음....0을 넣은부분처럼
def solve(n,q):
    if len(q) == 7:
        q.remove(0)
        print(*sorted(q))
        q.add(0)
    for i in range(n):
        if l[i] not in q and l[i] > max(q):
            q.add(l[i])
            solve(n,q)
            q.remove(l[i])
if __name__ == "__main__":
    while 1:
        l = list(map(int,input().split()))
        n=l.pop(0)
        if n == 0:
            break
        q = set([0])
        solve(n,q)
        print()



#https://ji-gwang.tistory.com/267

# def dfs(depth, idx):
#     if depth == 6:
#         print(*out)
#         return

#     for i in range(idx, k):#더 작은 수는 담지 않게 처리된 부분 내 코드에서 l[i] > max(q) 이 부분
#         out.append(S[i])
#         dfs(depth + 1, i + 1)
#         out.pop()#backtrack


# while True:
#     array = list(map(int, input().split()))
#     k = array[0]#요소의 개수
#     S = array[1:]#요소들
#     out = []#output
#     dfs(0, 0)
#     if k == 0:#0이면 종료
#         exit()#break와 같은 의미??
#     print()