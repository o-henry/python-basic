# itertools는 반복되는 데이터 처리기능을 포함하는 라이브러리


# permutations는 iterable객체 에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) 를 계산해준다.
# permutations는 클래스 이므로 겍체 초기화 이후 리스트 자료형으로 변환하여 사용한다.

from itertools import combinations_with_replacement
from itertools import product
from itertools import combinations
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 3))
print(result)


# combinations는 순서를 고려하지 않고 나열하는 모든 경우의 수(조합)를 계산한다.


data = ['A', 'B', 'C']
result = list(combinations(data, 2))

print(result)

# product는 permutation과 같이 순열을 계산하는데, 원소를 중복하여 뽑는다.
# product객체를 초기화 할때는 뽑고자 하는 데이터 개수를 repeat 속성값으로 넣어준다.


data = ['A', 'B', 'C']
result = list(product(data, repeat=2))
print(result)


# combinations_with_replacementsms 중복을 포함한 조합을 추출한다.


data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)
