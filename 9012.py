#9012
#gpt's solution
# """(s: str): 함수의 매개변수(parameter)를 나타내며, 여기서 s는 함수가 받아들일 입력 값이고, : str은 이 변수 s가 문자열 타입이어야 함을 명시합니다.-> bool: 이 부분은 함수의 반환값(return type)에 대한 타입 힌트입니다. 여기서 bool은 이 함수가 불리언(Boolean) 타입, 즉 True나 False를 반환할 것임을 의미합니다."""

#replit's code
def checkValidString(s: str) -> bool:
    balance = 0
    for char in s:
        if char == '(' or char == '*':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    balance = 0
    for char in reversed(s):
        if char == ')' or char == '*':
            balance += 1
        else:
          balance -= 1
        if balance < 0:
            return False
    return True




#파라미터로 s를 받을건데, s는 str타입이다.
#return값이 bool타입이다.
def check(s: str) -> bool:
  a = 0
  for i in s:
    if i == '(':
      a += 1
    elif i == ')':
      a -= 1
    if a < 0:
      return False
  a = 0
  for i in reversed(s):
    #(() 생각해보자! reversed 에서만 확인이된다.
    if i == ')':
      a += 1
    elif i == '(':
      a -= 1
    if a < 0:
      return False
  return True


def check2(s: str) -> bool:
  l=[]
  for i in s:
    if i == '(':
      l.append(i)
    elif i == ')':
      if l:
        l.pop()
      else:
        return False
  if not l:#l에 괄호가 없다면
    return True
if __name__ == "__main__":
  t = int(input())
  
  for _ in range(t):
    s = input()
    result = check2(s)
    if result:
      print("YES")
    else:
      print("NO")
