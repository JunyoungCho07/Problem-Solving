#이분탐색

# sample input
# 10 7
# 1 3 5 7 9 11 13 15 17 19

#재귀
def binary_search1(array, target, start, end):
  if start > end:
      return None
  mid = (start + end) // 2

  # 원하는 값 찾은 경우 인덱스 반환
  if array[mid] == target:
      return mid
  # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
  elif array[mid] > target:
      return binary_search1(array, target, start, mid - 1)
  # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
  else:#array[mid] < target
      return binary_search1(array, target, mid + 1, end)


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search1(array, target, 0, n - 1)
if result is None:
  print('원소가 존재 X')
else:
  #result는 0부터 센 값이므로, +1 해주어 1부터 센 값으로 보정
  print(result + 1)



#반복문
def binary_search2(array, target, start, end):
  while start <= end:
      mid = (start + end) // 2

      # 원하는 값 찾은 경우 인덱스 반환
      if array[mid] == target:#찾은경우
          return mid
      # 원하는 값이 중간점의 값보다 작은 경우 왼쪽 부분(절반의 왼쪽 부분) 확인
      elif array[mid] > target:#찾는 값보다 큰 경우
          end = mid - 1#최고점을 이 지점으로 설정
      # 원하는 값이 중간점의 값보다 큰 경우 오른쪽 부분(절반의 오른쪽 부분) 확인
      else:#array[mid] < target
          start = mid + 1#최소값을 이 지점으로 설정

  return None#start > end


n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search2(array, target, 0, n - 1)
if result is None:
  print('원소가 존재 X')
else:
  #result는 0부터 센 값이므로, +1 해주어 1부터 센 값으로 보정
  print(result + 1)




#https://velog.io/@kimdukbae/%EC%9D%B4%EB%B6%84-%ED%83%90%EC%83%89-%EC%9D%B4%EC%A7%84-%ED%83%90%EC%83%89-Binary-Search
