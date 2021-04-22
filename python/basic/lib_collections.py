# deque 를 사용해 큐를 구현한다.
# deque는 앞쪽에 원소를 추가하거나, 제거, 뒤쪽에 원소를 추가하거나 제거할때 모두 O(1)의 시간복잡도를 갖는다.
# 인덱싱, 슬라이싱을 사용할 수 없다.
# 스택이나 큐 기능을 모두 포함한다


from collections import Counter
from collections import deque

# O(1)
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)

print(data)
print(list(data))


# Counter는 등장횟수를 계산해준다.
# dict로 변환시 hashmap 처럼 작동하네..?
counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print(counter['blue'])
print(counter['red'])
print(dict(counter))


# >>> from collections import Counter
# >>>
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>>
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>>
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]
