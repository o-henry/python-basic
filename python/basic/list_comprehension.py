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
