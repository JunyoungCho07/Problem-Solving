arr = list(input())
sum = 10
for i in range(1, len(arr)):
    if arr[i] == arr[i-1]:
        sum += 5
    else:
        sum += 10
print(sum)