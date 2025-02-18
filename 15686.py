import sys
input = sys.stdin.readline

def dis(x1: int,y1: int,x2: int,y2: int) -> int:
    return abs(x1-x2) + abs(y1-y2)

def input_2d(n: int) -> list:#n*n
    l=[]
    for _ in range(n):
        l.append(list(map(int,input().split())))
    return l

def solve(lis: list) -> int:# lis는 오름차순 정렬된 데이터!
    # tmp = 99999999
    #else와 elif를 묶어서 위에 하나로 쓰기 가능 but 이해를 위해서 나누어 씀
    if len(lis) == m:
        chicken_dis=0
        for j in house_place:# 각 집에 대해서
            min_dis=float('inf')# 치킨집과의 거리 최소값
            for i in lis:# 각 치킨집과의 거리 계산
                x1,y1 = chicken_place[i]
                x2,y2 = j
                min_dis = min(min_dis,dis(x1,y1,x2,y2))
            chicken_dis += min_dis# 최소거리의 치킨집 -> 치킨거리 -> 더해줌
        return chicken_dis# 치킨거리의 총 합
    
    elif len(lis) == 0:# 처음 [] 가 들어왔을때 -> [0],[1],[2] ... 호출
        tmp = float('inf')
        for i in range(len(chicken_place)):
            tmp = min(tmp, solve([i]))# 치킨거리의 총 합 중에서 최소값 -> 재귀적으로 호출된 함수들의 최소값중에서 제일 최소값을 찾아줌.
        return tmp# 최소값 반환 ->> 최종 치킨거리
    
    else:# 기존 치킨집에 치킨지점 하나 더 추가!
        tmp = float('inf')
        for i in range(lis[-1]+1,len(chicken_place)):# 앞 치킨집보다 뒤에 있는 치킨집을 추가해줌(lis는 오름차순 정렬된 데이터터)
            tmp = min(tmp, solve(lis+[i]))# 치킨거리의 총 합 중에서 최소값
        return tmp# 최소값 반환

if __name__ == '__main__':
    n,m = map(int,input().split())
    # 0 빈자리
    # 1 집
    # 2 치킨집
    l = input_2d(n)# 지도 입력 받음
    # m 남길 치킨집의 개수

    chicken_place = [[x,y] for x in range(n) for y in range(n) if l[x][y]==2]# 치킨집의 위치
    house_place = [[x,y] for x in range(n) for y in range(n) if l[x][y]==1]# 집의 위치

    print(solve([]))






#MS copilot
'''
combinations 함수는 파이썬의 itertools 모듈에 포함된 함수로, 
주어진 iterable(반복 가능한 객체)에서 특정 길이의 모든 조합을 생성하는 함수입니다. 
예를 들어, 리스트 [1, 2, 3]에서 길이 2의 모든 조합을 구하면 (1, 2), (1, 3), (2, 3)과 같이 생성됩니다
'''
'''
import sys
from itertools import combinations

input = sys.stdin.readline

def calculate_distance(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

def get_city_map(n):
    city_map = []
    for _ in range(n):
        city_map.append(list(map(int, input().split())))
    return city_map

def find_min_chicken_distance(houses, chickens, m):
    min_distance = float('inf')
    
    # 치킨집의 모든 조합을 생성합니다.
    for chicken_comb in combinations(chickens, m):
        total_distance = 0
        
        # 각 집에 대해 가장 가까운 치킨집의 거리를 구합니다.
        for house in houses:
            min_distance_to_chicken = float('inf')
            for chicken in chicken_comb:
                min_distance_to_chicken = min(min_distance_to_chicken, calculate_distance(house, chicken))
            total_distance += min_distance_to_chicken
        
        # 현재 조합에서의 총 치킨 거리가 최소 거리인지 확인합니다.
        min_distance = min(min_distance, total_distance)
    
    return min_distance

if __name__ == '__main__':
    city_size, max_chickens = map(int, input().split())
    city_map = get_city_map(city_size)

    chicken_locations = []
    house_locations = []

    for r in range(city_size):
        for c in range(city_size):
            if city_map[r][c] == 2:
                chicken_locations.append((r, c))
            elif city_map[r][c] == 1:
                house_locations.append((r, c))

    result = find_min_chicken_distance(house_locations, chicken_locations, max_chickens)
    print(result)
'''