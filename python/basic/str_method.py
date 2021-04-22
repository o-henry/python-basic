https: // docs.python.org/2/library/stdtypes.html  # str.isupper

# str.isalnum()
# Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise.
# For 8-bit strings, this method is locale-dependent.

# str.isalpha()
# Return true if all characters in the string are alphabetic and there is at least one character, false otherwise.
# For 8-bit strings, this method is locale-dependent.

# str.isdigit()
# Return true if all characters in the string are digits and there is at least one character, false otherwise.
# For 8-bit strings, this method is locale-dependent.

# str.islower()
# Return true if all cased characters 4 in the string are lowercase and there is at least one cased character, false otherwise.
# For 8-bit strings, this method is locale-dependent.

# str.isupper()
# Return true if all cased characters 4 in the string are uppercase and there is at least one cased character, false otherwise.
# For 8-bit strings, this method is locale-dependent.

# str.capitalize()
# Return a copy of the string with its first character capitalized and the rest lowercased.
# For 8-bit strings, this method is locale-dependent.

# str.swapcase()
# Return a copy of the string with uppercase characters converted to lowercase and vice versa.
# For 8-bit strings, this method is locale-dependent.
a = 'HeLLow wOrld'
a = a.swapcase()
print(a)

# str.startswith(prefix[, start[, end]])
# 문자열이 지정된 prefix 로 시작하면 True 를 돌려주고, 그렇지 않으면 False 를 돌려줍니다.
# prefix 는 찾고자 하는 접두사들의 튜플이 될 수도 있습니다. 선택적 start 가 제공되면 그 위치에서 검사를 시작합니다.
# 선택적 end 를 사용하면 해당 위치에서 비교를 중단합니다.

# slicing
# s[i:j] slice of s from i to j (3)(4)
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = 'Helloworld'
# [2,3,4]
print(a[1:4])
# ll
print(b[2:4])

a = 'Hello'
b = 'World'
print(a + ' ' + b)
print(a * 3)
print(a[2: 4])

# str.split(sep=None, maxsplit=-1)
# sep 를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트를 돌려줍니다.
# maxsplit 이 주어지면 최대 maxsplit 번의 분할이 수행됩니다 (따라서, 리스트는 최대 maxsplit+1 개의 요소를 가지게 됩니다). maxsplit 이 지정되지 않았거나 -1 이라면 분할 수에 제한이 없습니다 (가능한 모든 분할이 만들어집니다).
