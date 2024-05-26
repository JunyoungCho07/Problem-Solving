t = int(input())
l=[]
for i in range(t):
    l.append(int(input()))
if l.count(0) > l.count(1):
    print('Junhee is not cute!')
else:
    print("Junhee is cute!")