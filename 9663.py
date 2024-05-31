#9663
def solve(row, n):
  global sum
  if row >= n:
    sum += 1
    return
  else:
    for i in range(n):
      if not col[i] and not inc[row+i] and not dec[row-i+n-1]:
        col[i] = inc[row+i] = dec[row-i+n-1] = 1
        solve(row+1, n)
        col[i] = inc[row+i] = dec[row-i+n-1] = 0


if __name__ == '__main__':
  n = int(input())
  sum = 0
  col = [0] * n
  inc = [0] * (2*n-1)
  dec = [0] * (2*n-1)  
  solve(0, n)
  print(sum)
