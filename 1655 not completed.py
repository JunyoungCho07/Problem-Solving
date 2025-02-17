#최대힙 최소힙
import sys
input = sys.stdin.readline

def mid(a):
    if a % 2 == 0:
        return a//2 -1
    else:
        return a//2

def solve():
    for i in range(n):
        bin_app(l,int(input()))
        print(l)
        print(l[mid(len(l))])

def bin_app(l,num):
    s=0
    e=len(l)-1
    if len(l) == 0:
        l.append(num)
        return
    else:
        while l[s]<l[e]:
            p = (s+e)//2
            if l[p] >= l[-1]:
                e = p
            else:
                s = p
    l.insert(s,num)
    

if __name__ == '__main__':
    n = int(input())
    l = []
    solve()