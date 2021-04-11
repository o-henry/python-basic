# 사전자료형 key value 쌍의 데이터  데이터의 검색 및 수정에 있어서 O(1)의 시간 처리를 한다.
# 파이썬의 딕셔너리는 내부적으로 해시테이블을 사용한다.


data = dict()
data['사과'] = 'Apple'
data['포도'] = 'Graph'
data['바나나'] = 'Banana'

print(data)

if '사과' in data:
    print('사과가 존재합니다.')

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])
