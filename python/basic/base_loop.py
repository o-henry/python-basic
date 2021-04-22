i = 1
result = 0

while i <= 9:
    result += i
    i += 1
print(result)


for i in range(2, 10):
    for j in range(1, 10):
        print(i, 'X', j, '=', i*j)
    print()


scores = [90, 85, 77, 65, 87]
black_list = {2, 4}

for i in range(5):
    if i+1 in black_list:
        continue
    if scores[i] >= 80:
        print(i+1, '번 학생은 합격입니다.')
