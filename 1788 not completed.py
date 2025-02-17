#메모리 초과 뜸...
import sys
input = sys.stdin.readline

n= int(input())
positive = True if n>0 else False
n = abs(n)
if positive:
    dpp= [0,1]
    for i in range(2,n+1):
        dpp.append(dpp[i-1]+dpp[i-2])
else:
    dpm = [0,1]
    for i in range(2,n+1):
        dpm.append(dpm[i-2] - dpm[i-1])

l = dpp if positive else dpm
if l[n] > 0: print(1)
elif l[n] == 0: print(0)
else: print(-1)
print(abs(l[n])%1000000000)

