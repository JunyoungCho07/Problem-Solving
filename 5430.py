#R:reverse
#D:delete from front
import sys
input = sys.stdin.readline

def op(p, l):
    reverse = False#뒤집어 졌냐
    for op in p:
        if op == 'R':
            reverse = not reverse#not으로 뒤집는다
        elif op =='D':
            if not l:
                return 'error' #비었는데 pop연산 시행할 경우 error return
            if reverse:
                l.pop()#뒤집어 진 경우 뒤에서 pop
            else:
                l.pop(0)#안 뒤집어 진 경우 앞에서 pop
    if reverse:
        l = l[::-1]#마지막에 뒤집어진 여부에 따라 0번이나 1번만 뒤집음 -> 뒤집는 연산 최소화 -> 효율 up
    return l#연산이 끝난 리스트 리턴

t = int(input())
for i in range(t):
    p = input().strip()#operation
    n = int(input())
    arr_input = input().strip()#마지막에 널 문자도 같이 들어가기에 strip해줌
    if arr_input == '[]':
        l = []
    else:
        l = list(map(int, arr_input[1:-1].split(',')))
    result = op(p,l)
    if result == 'error':
        print('error')
    else:
        print(f"[{','.join(map(str,result))}]")#결과 리스트를 문자로 변환 후 , 로 구분하여 출력
