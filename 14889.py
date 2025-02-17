import sys
input = sys.stdin.readline

def solve(n: int,lst: list):
    if len(lst) == n//2:
        team1 = lst
        team2 = list(set([i for i in range(n)])-set(lst)) #차집합 사용
        team1_score = cal(team1)
        team2_score = cal(team2)
        res.append(abs(team1_score-team2_score))
        return
    elif lst[-1] == n: #마지막 원소가 포함되었지만 인원수 채우지 못함
        return
    else:
        for i in range(lst[-1]+1,n): #다음 학생부터 차례로 포함시켜줌
            solve(n,lst+[i])
            # print(n,lst+[i])

def cal(team: list) -> int:
    sum = 0
    for i in range(len(team)): #앞 인덱스 i
        for j in range(i+1,len(team)): #뒤 인덱스 j
            sum += S[team[i]][team[j]] + S[team[j]][team[i]]
            #각 학생정보를 불러와서 종합치 더해줌
    return sum

n = int(input())
S = []
res = []
for i in range(n):
    S.append(list(map(int, input().split())))
solve(n,[0])
# print(res)
print(min(res)) #종합치의 차이의 최솟값



#MS copilot version
'''
import sys
input = sys.stdin.readline

def solve(n: int, lst: list, min_diff: int) -> int:
    if len(lst) == n // 2:
        team1 = lst
        team2 = [i for i in range(n) if i not in lst]
        team1_score = cal(team1)
        team2_score = cal(team2)
        return min(min_diff, abs(team1_score - team2_score))
    
    if lst and lst[-1] == n - 1:
        return min_diff
    
    start = lst[-1] + 1 if lst else 0
    for i in range(start, n):
        min_diff = solve(n, lst + [i], min_diff)
    
    return min_diff

def cal(team: list) -> int:
    total_score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            total_score += S[team[i]][team[j]] + S[team[j]][team[i]]
    return total_score

try:
    n = int(input().strip())
    if n % 2 != 0:
        raise ValueError("n은 짝수여야 합니다.")
    S = []
    for _ in range(n):
        S.append(list(map(int, input().split())))

    min_diff = solve(n, [], float('inf'))
    print(min_diff)
except ValueError as e:
    print(e)
'''