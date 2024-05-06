#4949

import sys
input = sys.stdin.readline
dic = {")":"(", "}":"{","]":"["}#매치되는 애 비교
while 1:
  string = input().strip()#strip이유 밑에 참조
  if string[0] == ".":
    break
  parenthesis = []
  #chk는 no가 출력된 이후 다시 yes나 no가 출력돼면 안되기에 도입
  chk = True
  for i in range(len(string)):
    if string[i] == "(" or string[i] == "{" or string[i] == "[":# 줄이면 if string[i] in "({["
      parenthesis.append(string[i])
    elif string[i] == ")" or string[i] == "}" or string[i] == "]":# 줄이면 if string[i] in ")}]"
      if len(parenthesis) == 0:#닫힌게 더 많아 pop불가능
        print("no")
        chk = False
        break
      top = parenthesis.pop()
      if top != dic[string[i]]:#괄호 매치 X
        print("no")
        chk = False
        break
  if len(parenthesis) == 0 and chk:#남아있는 괄호가 없고, while문에서 break로 나오지 않을 경우(chk == True)
    print("yes")
  elif chk:#생각 못했던 부분
    #chk가 True더라도 parenthesis가 남아있어 매치 안된 괄호가 있을 수 있음
    print("no")





#by GPT4.0
# import sys
# input = sys.stdin.readline
    
# """input().strip()을 사용하는 주된 이유는 입력에서 앞뒤의 공백이나 줄바꿈 문자(\n)를 제거하기 위해서입니다. 특히, 파이썬에서 input() 함수를 사용하여 입력을 받을 때, 입력 라인의 끝에 자동으로 포함되는 줄바꿈 문자를 제거하는 용도로 많이 사용됩니다.
# 이렇게 입력받은 문자열에서 자동으로 추가되는 줄바꿈을 제거함으로써, 문자열을 처리하는 코드가 더욱 정확하게 동작할 수 있도록 합니다. 예를 들어, 조건문에서 특정 문자열을 검사하거나, 입력 종료 조건으로 사용할 때 .strip() 없이는 예상치 못한 결과가 발생할 수 있습니다. 게다가, 앞뒤 공백을 제거하므로 사용자가 실수로 입력한 불필요한 공백에 의한 오류를 방지할 수 있습니다."""
    
# while True:
#   string = input().strip()
#   # print(string)
#   if string == ".":
#     break
#   parenthesis = []
#   balanced = True
#   for char in string:
#     if char in "({[":
#       parenthesis.append(char)
#     elif char in ")}]":
#       if not parenthesis:
#         print("no")
#         balanced = False
#         break
#       top = parenthesis.pop()
#       if (top == '(' and char != ')') or (top == '{' and char != '}') or (top == '[' and char != ']'):
#         print("no")
#         balanced = False
#         break
#   if balanced and not parenthesis:
#     print("yes")
#   elif balanced:#balanced = True but parenthesis is not empty
#     print("no")
