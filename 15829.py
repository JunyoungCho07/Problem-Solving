#15829
# print(ord("a")) --> 97
#a=1 --> ord-9
t = int(input())
s = input()
sum=0
for i in range(t):
  sum += (ord(s[i]) - 96) * (31**i)
print(sum %1234567891)
