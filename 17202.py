from collections import deque
l = deque()
n1 = input()
n2 = input()
for i in range(8):
    l.append(int(n1[i]))
    l.append(int(n2[i]))
while len(l) != 2:
    for i in range(len(l)-1):
        l[i] = (l[i] + l[i+1]) % 10
    l.pop()
print(f'{l[0]}'+f'{l[1]}')
