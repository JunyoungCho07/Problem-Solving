#deque 사용
import sys
from collections import deque
input = sys.stdin.readline
#커서 오른쪽 왼쪽 구분
a = input().strip()#a = input().split()했다가 틀림
#input().split()은 리스트를 반환
#input().strip()은 문자열을 반환
#example input: abcd
#input().split() # ['abcd']
#input().strip() # 'abcd'
left_stack=deque(a)
#deque는 반복 가능한 객체를 받아서 각각의 요소를 덱의 요소로 만든다
#ex)
#deque('abcd') -> deque(['a','b','c','d']) 이렇게 저장됨
#그래서 요소 하나하나에 대해서 pop과 append연산이 가능하게 되는 것
right_stack=deque()
t= int(input())
for _ in range(t):
    l = input().split()
    if l[0] == 'L':
        if left_stack:
            right_stack.appendleft(left_stack.pop())
    if l[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.popleft())
    if l[0] == 'B':
        if left_stack:
            left_stack.pop()
    if l[0] == 'P':
        left_stack.append(l[1])
print(''.join(left_stack)+''.join(right_stack))









#내가 처음 짠 코드
#인덱스의 왼쪽 을 가르키는 커서이다.
# import sys
# input = sys.stdin.readline
# a = input()
# string = []
# for i in range(len(a)):
#     string.append(a[i])
# pointer = len(string)
# #0 <= pointer <= len(string)
# t = int(input())
# for _ in range(t):
#     l = list(map(str,input().split()))
#     if l[0] == 'L':
#         if pointer != 0:
#             pointer -= 1
#     if l[0] == 'D':
#         if pointer != len(string):
#             pointer += 1
#     if l[0] == 'B':
#         if pointer == 0:
#             pass
#         else:
#             string.pop(pointer-1)
#             pointer -= 1
#     if l[0] == 'P':
#         string.insert(pointer, l[1])
#         pointer += 1
# print(''.join(string))
#시간초과남