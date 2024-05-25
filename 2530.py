h,m,s = map(int, input().split())
sp = int(input())

# h = h + sp//3600
# sp = sp%3600
# m = m+ sp//60
# sp = sp%60
s = s+ sp

while 1:
    if s >= 60:
        m += 1
        s -= 60
    if m >= 60:
        h += 1
        m -= 60
    if h >= 24:
        h -= 24
    if m < 60 and s < 60 and h <24:
        break
print(h,m,s,sep=' ')