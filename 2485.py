import sys

def gcd(a,b):
    while b:
        c = a%b
        a,b=b,c
    return a

if __name__ == '__main__':
    input = sys.stdin.readline
    n = int(input())
    l = []
    for i in range(n):
        l.append(int(input()))
    
    dis=[l[i+1]-l[i] for i in range(n-1)]
    
    a = gcd(dis[0],dis[1])
    for i in range(2,len(dis)):
        a = gcd(a,dis[i])
    #a = 최대 공약수 GCD
    
    print(((l[-1]-l[0])//a)-len(l)+1)
