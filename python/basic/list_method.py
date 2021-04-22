# make list
# 크기가 N인 1차원 리스트 초기화
n = 10
a = [0] * n

# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(a)

# remove list
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set]
print(result)


# list comprehension
# 리스트 초기화 방법중 하나, 특정 조건에 해당하는 리스트를 생성할 수 있다.
# 2차원 리스트를 초기화 할때 매우 효과적이다.

array = [i for i in range(20) if i % 2 == 1]

# [1,3,5,7, ... , 19]
print(array)

array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)


# for 앞이 결과값(피연산자)
square = [i * i for i in range(1, 10)]


# N X M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
temp = [[0] * m] * n
print(array)
print(temp)


# list method
a = [1, 4, 3]
print('base: ', a)

# O(1) 파이썬의 리스트는 연결리스트다.
a.append(2)
print('append: ', a)

# 오름차순 O(NlogN)
a.sort()
print('sort: ', a)

# 내림차순
a.sort(reverse=True)
print('내림차순: ', a)

# O(N)
a.reverse()
print('reverse: ', a)

# O(N) 특정 인덱스에 원소 삽입
a.insert(2, 3)
print('인덱스 2에 3 추가: ', a)

# O(N) 특정 값 데이터 개수 세기
print('값이 3인 데이터 개수: ', a.count(3))

# O(N) 특정 값 삭제
a.remove(1)
print('값이 1인 데이터 삭제: ', a)
