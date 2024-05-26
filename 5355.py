t = int(input())
for i in range(t):
    l = list(map(str, input().split()))
    n = float(l.pop(0))
    for op in l:
        if op == '@':
            n *= 3
        elif op == '#':
            n -= 7
        elif op == '%':
            n += 5
    print("{0:.2f}".format(n))