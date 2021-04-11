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
